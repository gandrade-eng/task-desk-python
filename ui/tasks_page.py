from config import THEMES, LANGUAGES

from PySide6.QtCore import QSize, Signal
from PySide6.QtGui import Qt, QIcon
from PySide6.QtWidgets import (
    QMainWindow, QFrame, QHBoxLayout, 
    QVBoxLayout, QSpacerItem, QSizePolicy, 
    QLabel, QWidget, QStackedWidget, 
    QApplication, QPushButton, QCheckBox,
    QProgressBar, QLineEdit, QComboBox,
    QScrollArea, QMenu, QMessageBox
)

class TasksPage(QWidget):
    def __init__(self, settings, task_manager, history_manager):
        super().__init__()

        self.settings = settings
        self.task_manager = task_manager
        self.history_manager = history_manager

        self.create_page_tasks()

    # Page Tasks
    # //////////////////////////////////////////////////////////
    def create_page_tasks(self):
        self.page_tasks = QVBoxLayout(self)

        self.create_task_list()

        self.create_tasks_statistics()

        self.page_tasks.addWidget(self.page_tasks_list)
        self.page_tasks.addWidget(self.page_tasks_statistics)

        self.apply_theme()

        self.refresh()

    # Tasks List
    # //////////////////////////////////////////////////////////
    def create_task_list(self):
        # Titulo
        # Pesquisa
        # Filtros

        # Criar/Editar/Excluir
        # Todas as Tarefas
        self.page_tasks_list = QFrame()
        self.page_tasks_list_layout = QVBoxLayout(self.page_tasks_list)

        self.create_tasks_header()

        self.create_tasks_filters()

        self.create_list_container()

        self.page_tasks_list_layout.addWidget(self.tasks_header)
        self.page_tasks_list_layout.addWidget(self.tasks_filters)
        self.page_tasks_list_layout.addWidget(self.tasks_scroll)

    # Tasks Header
    def create_tasks_header(self):
        self.tasks_header = QFrame()
        self.tasks_header_layout = QHBoxLayout(self.tasks_header)

        self.tasks_header_title = QLabel("Todas as Tarefas")
        self.tasks_header_title.setStyleSheet("color: black")

        self.tasks_header_button = QPushButton("➕ Adicionar")
        self.tasks_header_button.setObjectName("tasks_header_button")
        self.tasks_header_button.setMaximumWidth(160)

        self.tasks_header_layout.addWidget(self.tasks_header_title)
        self.tasks_header_layout.addWidget(self.tasks_header_button)

    # Tasks Filters
    def create_tasks_filters(self):
        self.tasks_filters = QFrame()
        self.tasks_filters_layout = QVBoxLayout(self.tasks_filters)

        self.tasks_filter_search = QLineEdit()

        # Todos
        # Pendentes
        # Concluídas
        self.tasks_filters_status = QComboBox()

        # Todas
        # Hoje
        # Amanhã 
        # Próximas
        # Atrasadas
        self.tasks_filters_date = QComboBox()

        # Data ↑
        # Data ↓
        # Nome A-Z
        # Nome Z-A
        self.tasks_filters_order = QComboBox()

        self.tasks_filters_box_layout = QHBoxLayout()
        self.tasks_filters_box_layout.addWidget(self.tasks_filters_status)
        self.tasks_filters_box_layout.addWidget(self.tasks_filters_date)
        self.tasks_filters_box_layout.addWidget(self.tasks_filters_order)

        self.tasks_filters_layout.addWidget(self.tasks_filter_search)
        self.tasks_filters_layout.addLayout(self.tasks_filters_box_layout)

    # List Container
    def create_list_container(self):
        self.list_container = QFrame()
        self.list_container.setObjectName("list_container")
        self.list_container.setStyleSheet("background-color: white; border: 1px solid black;")
        self.list_container_layout = QVBoxLayout(self.list_container)

        self.tasks_scroll = QScrollArea()
        self.tasks_scroll.setStyleSheet("""
            QScrollArea {
                background-color: white;
                border: none;
            }
        """)
        self.tasks_scroll.setWidgetResizable(True)
        self.tasks_scroll.setWidget(self.list_container)

    # Load Tasks
    def load_tasks(self):
        history_tasks = self.history_manager.get_tasks()

        for task in history_tasks:
            self.create_task_card(task)

        self.list_container_layout.addStretch()

    # Task Card
    def create_task_card(self, task):
        task_id = task.id

        frame_task = QFrame()
        frame_task.setObjectName("frame_task")
        frame_task.setMinimumSize(280, 60)
        frame_task.setMaximumSize(500, 80)

        frame_task_layout = QHBoxLayout(frame_task)

        page_task_text = QLabel(
            f"{task.title}\nHora: {task.time.toString('HH:mm')}"
        )
        page_task_text.setObjectName("page_task_text")
        page_task_text.setStyleSheet("color: black")

        # Riscar
        font = page_task_text.font()
        font.setStrikeOut(True)
        page_task_text.setFont(font)

        page_task_text2 = QLabel(task.date.toString("dd/MM"))
        page_task_text2.setObjectName("page_task_text2")
        page_task_text2.setStyleSheet("color: black")

        options_button = QPushButton("⋮")
        options_button.setFixedSize(35, 35)
        options_button.setStyleSheet("""
            QPushButton {
                border: none;
                color: #6B7280;
                font-size: 22px;
                background-color: transparent;
                border-radius: 6px;
            }

            QPushButton:hover {
                background-color: #F3F4F6;
                color: #111827;
            }

            QPushButton:pressed {
                background-color: #E5E7EB;
            }
        """)

        options_button.clicked.connect(
            lambda: self.show_task_options(task_id, options_button)
        )

        frame_task_layout.addWidget(page_task_text)
        frame_task_layout.addStretch()
        frame_task_layout.addWidget(page_task_text2)
        frame_task_layout.addWidget(options_button)

        self.list_container_layout.addWidget(frame_task)

    # Tasks Statistics
    # //////////////////////////////////////////////////////////
    def create_tasks_statistics(self):
        self.page_tasks_statistics = QFrame()
        self.page_tasks_statistics.setMinimumHeight(200)
        self.page_tasks_statistics_layout = QHBoxLayout(self.page_tasks_statistics)

        self.create_overall_progress()

        self.create_history_statistics()

        self.create_general_status()

        self.page_tasks_statistics_layout.addWidget(self.overall_progress)
        self.page_tasks_statistics_layout.addWidget(self.history_statistics)
        self.page_tasks_statistics_layout.addWidget(self.general_status)

    # Overall Progress
    def create_overall_progress(self):
        # Taxa de conclusão
        # ████████░░ 82%
        # 82% das tarefas criadas foram concluídas

        self.overall_progress = QFrame()
        self.overall_progress.setObjectName("overall_progress")
        self.overall_progress.setMinimumWidth(180)
        self.overall_progress.setMaximumHeight(200)
        self.overall_progress.setStyleSheet("color: black; border-radius: 5px; border: 1px solid black;")
        self.overall_progress_layout = QVBoxLayout(self.overall_progress)

        stats = self.history_manager.get_task_completion_percentage(self.history_manager.get_tasks())

        # percentage = 0
        # if stats["total"] > 0:
        #     percentage = int(stats["completed"] / stats["total"] * 100)
        # self.completion_bar.setValue(percentage)
        # self.completion_label.setText(
        #     f"{percentage}% das tarefas criadas foram concluídas."
        # )

        text_one = QLabel("Taxa de conclusão")
        text_one.setStyleSheet("color: black; border-radius: 5px; border: 1px solid black;")

        completion_bar = QProgressBar()
        completion_bar.setMinimum(0)
        completion_bar.setMaximum(100)
        completion_bar.setValue(stats)
        completion_bar.setTextVisible(True)
        completion_bar.setFormat("%p%")
        completion_bar.setStyleSheet("""
            QProgressBar {
                border: 1px solid #888;
                border-radius: 5px;
                text-align: center;
                height: 18px;
            }
        
            QProgressBar::chunk {
                background-color: #4CAF50;
                border-radius: 4px;
            }""")

        text_two = QLabel(f"{stats}% das tarefas criadas\nforam concluídas")
        text_two.setStyleSheet("color: black; border-radius: 5px; border: 1px solid black;")

        self.overall_progress_layout.addWidget(text_one)
        self.overall_progress_layout.addWidget(completion_bar)
        self.overall_progress_layout.addWidget(text_two)

    # History Statistics
    def create_history_statistics(self):
        # Tarefas criadas:
        # Janeiro    32
        # Fevereiro  45
        # Março      27
        # Abril      51

        # history

        self.history_statistics = QFrame()
        self.history_statistics.setObjectName("history_statistics")
        self.history_statistics.setStyleSheet("color: black; border-radius: 5px; border: 1px solid black;")
        self.history_statistics.setMinimumWidth(200)
        self.history_statistics.setMaximumHeight(220)
        self.history_statistics_layout = QVBoxLayout(self.history_statistics)

        self.history_statistics_title = QLabel("Tarefas Criadas:")

        self.history_statistics_months_layout = QHBoxLayout()

        self.history_statistics_left = QVBoxLayout()
        self.history_statistics_right = QVBoxLayout()

        months = [
            "january",
            "february",
            "march",
            "april",
            "may",
            "june",
            "july",
            "august",
            "september",
            "october",
            "november",
            "december"
        ]

        for i, month in enumerate(months):
            month_label = QLabel(month)
            month_label.setMinimumWidth(100)
            month_label.setMaximumHeight(120)
            month_label.setStyleSheet("color: black; border-radius: 5px; border: 1px solid black;")

            if i < 6:
                self.history_statistics_left.addWidget(month_label)
            else:
                self.history_statistics_right.addWidget(month_label)

        self.history_statistics_months_layout.addLayout(self.history_statistics_left)
        self.history_statistics_months_layout.addLayout(self.history_statistics_right)

        self.history_statistics_layout.addWidget(self.history_statistics_title)
        self.history_statistics_layout.addLayout(self.history_statistics_months_layout)

    # General Status
    def create_general_status(self):
        # Total
        # 245 tarefas
        # Concluídas 180
        # Pendentes 40
        # Atrasadas 25

        status = self.history_manager.get_task_statistics(self.history_manager.get_tasks())

        self.general_status = QFrame()
        self.general_status.setStyleSheet("color: black; border-radius: 5px; border: 1px solid black;")
        self.general_status.setMinimumWidth(200)
        self.general_status.setMaximumHeight(220)
        self.general_status_layout = QVBoxLayout(self.general_status)

        self.general_status_title = QLabel("Total")
        self.general_status_nTasks = QLabel(f"{status["total"]} Tarefas")
        self.general_status_completed = QLabel(f"{status["completed"]} Concluidas")
        self.general_status_incomplete = QLabel(f"{status["incomplete"]} Pendentes")

        self.general_status_layout.addWidget(self.general_status_title)
        self.general_status_layout.addWidget(self.general_status_nTasks)
        self.general_status_layout.addWidget(self.general_status_completed)
        self.general_status_layout.addWidget(self.general_status_incomplete)

    # Refresh
    # //////////////////////////////////////////////////////////
    def refresh(self):
        self.clear_layout(self.list_container_layout)

        self.load_tasks()

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)

            if item.widget():
                item.widget().deleteLater()

            elif item.layout():
                self.clear_layout(item.layout())

    # Clicked
    # //////////////////////////////////////////////////////////
    def show_task_options(self, task_id, options_button):
        menu = QMenu(self)
        menu.setStyleSheet("""
            QMenu {
                background-color: white;
                border: 2px solid #E5E7EB;
                border-radius: 8px;
                padding: 6px;
            }

            QMenu::item {
                background-color: transparent;
                color: #374151;
                padding: 8px 20px 8px 12px;
                border-radius: 6px;
                font-size: 14px;
            }

            QMenu::item:selected {
                background-color: #F3F4F6;
                color: #111827;
            }

            QMenu::separator {
                height: 1px;
                background-color: #E5E7EB;
                margin: 5px 8px;
            }
        """)

        edit_action = menu.addAction("✏️  Editar")
        # self.edit_task.connect(self.open_edit_task)

        details_action = menu.addAction("ℹ️  Detalhes")

        delete_action = menu.addAction("🗑️  Excluir")
        delete_action.triggered.connect(
            lambda: self.confirm_delete_task(task_id)
        )

        pos = options_button.mapToGlobal(
            options_button.rect().bottomLeft()
        )

        menu.exec(pos)

    def confirm_delete_task(self, task_id):
        reply = QMessageBox.question(
            self,
            "Excluir tarefa",
            "Tem certeza que deseja excluir esta tarefa?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.task_manager.remove_task(task_id)
            self.refresh()

    # Apply Theme
    # //////////////////////////////////////////////////////////
    def apply_theme(self):
        # self.styles = THEMES[self.settings["theme"]]

        # self.setStyleSheet(self.styles["tasks_page"])
        ...