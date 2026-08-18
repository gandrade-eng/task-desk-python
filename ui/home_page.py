# external imports
from PySide6.QtCore import Signal, QDate, QSize
from PySide6.QtGui import Qt, QTextCharFormat, QColor, QIcon
from PySide6.QtWidgets import (
    QFrame, QHBoxLayout, QVBoxLayout, 
    QLabel, QWidget, QPushButton, QCheckBox,
    QCalendarWidget, QGraphicsDropShadowEffect,
    QToolButton, QMenu, QMessageBox, QScrollArea
)

# internal imports
from config import THEMES, LANGUAGES

class HomePage(QWidget):
    add_task_page_requested = Signal()
    task_options = Signal(int, QPushButton)
    edit_task_requested = Signal(int)

    def __init__(self, settings, task_manager, history_manager):
        super().__init__()

        self.task_options.connect(self.show_task_options)

        self.settings = settings
        self.task_manager = task_manager
        self.history_manager = history_manager

        self.create_page_home()

    # Page Home
    # //////////////////////////////////////////////////////////
    def create_page_home(self):
        self.page_home_layout = QHBoxLayout(self)
        self.page_home_layout.setContentsMargins(25,25,25,25)

        # Page Home Main
        self.create_page_home_main()

        # Page Home Side
        self.create_page_home_side()

        self.page_home_layout.addLayout(self.page_home_main_layout)
        self.page_home_layout.addWidget(self.page_home_side)

        # label_page_home.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.label.setText(f"✓ Tarefas - {self.num_tarefas}")

        # def atualizar_total_tarefas(self):
        # total = len(self.tasks)
        # self.label.setText(f"✓ Tarefas - {total}")
        # self.tasks.append(nova_tarefa)
        # self.atualizar_total_tarefas()

        self.apply_theme()

        self.refresh()

    # Home Main
    # //////////////////////////////////////////////////////////
    def create_page_home_main(self):
        self.page_home_main_layout = QVBoxLayout()
        self.page_home_main_layout.setAlignment(Qt.AlignTop)
        self.page_home_main_layout.setSpacing(15)

        self.header_text = QLabel("Tarefas")
        self.header_text.setObjectName("header_text")
        self.header_button = QPushButton("➕ Adicionar")
        self.header_button.setObjectName("header_button")
        self.header_button.setMaximumWidth(160)
        self.header_button.clicked.connect(self.add_task_page_requested.emit)

        self.page_home_main_header_layout = QHBoxLayout()
        self.page_home_main_header_layout.addWidget(self.header_text)
        self.page_home_main_header_layout.addWidget(self.header_button)
        self.page_home_main_layout.addLayout(self.page_home_main_header_layout)


        # MUDAR DPS POR FAVOR
        self.today_tasks_text = QLabel(f"🔥 Tarefas de Hoje - {len(self.task_manager.get_today_tasks())}")
        self.today_tasks_text.setObjectName("today_tasks_text")
        self.page_home_main_layout.addWidget(self.today_tasks_text)

        self.today_tasks_container = QWidget()
        self.today_tasks_layout = QVBoxLayout(self.today_tasks_container)
        self.today_tasks_layout.setAlignment(Qt.AlignTop)

        self.today_tasks_scroll = QScrollArea()
        self.today_tasks_scroll.setStyleSheet("""
            QScrollArea {
                background: transparent;
                border: none;
            }

            QScrollArea > QWidget > QWidget {
                background: transparent;
            }

            QScrollBar:vertical {
                background: #F3F4F6;
                width: 8px;
                margin: 2px 2px 2px 2px;
                border-radius: 4px;
            }

            QScrollBar::handle:vertical {
                background: #C9CDD2;
                min-height: 30px;
                border-radius: 4px;
            }

            QScrollBar::handle:vertical:hover {
                background: #AEB4BB;
            }

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                height: 0px;
            }

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: transparent;
            }
        """)
        self.today_tasks_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.today_tasks_scroll.setWidgetResizable(True)
        self.today_tasks_scroll.setWidget(self.today_tasks_container)

        self.page_home_main_layout.addWidget(self.today_tasks_scroll)

        # MUDAR DPS POR FAVOR
        self.upcoming_tasks_text = QLabel(f"⏰ Proximas Tarefas - {len(self.task_manager.get_upcoming_tasks(None))}")
        self.upcoming_tasks_text.setObjectName("upcoming_tasks_text")
        self.page_home_main_layout.addWidget(self.upcoming_tasks_text)

        self.upcoming_tasks_layout = QVBoxLayout()
        self.upcoming_tasks_layout.setSpacing(15)
        self.upcoming_tasks_layout.setAlignment(Qt.AlignTop)
        self.page_home_main_layout.addLayout(self.upcoming_tasks_layout)

    # Load Tasks
    def load_tasks(self):
        today_tasks = self.task_manager.get_today_tasks()

        for task in today_tasks:
            self.create_task_card(task, self.today_tasks_layout)

        upcoming_tasks = self.task_manager.get_upcoming_tasks(3)

        for task in upcoming_tasks:
            self.create_task_card(task, self.upcoming_tasks_layout)

    # Task Card
    def create_task_card(self, task, layout):
        task_id = task.id
        frame_home = QFrame()
        frame_home.setObjectName("frame_home")
        frame_home.setMinimumSize(280, 60)
        frame_home.setMaximumSize(500, 80)

        page_home_text = QLabel(f"{task.title}\nHora: {task.time.toString('HH:mm')}")
        page_home_text.setObjectName("page_home_text")

        if task.is_completed:
            page_home_text.setStyleSheet(
                "text-decoration: line-through;"
            )

        page_home_button = QCheckBox()
        page_home_button.setObjectName("page_home_button")
        page_home_button.setChecked(task.is_completed)
        page_home_button.toggled.connect(
            lambda checked, t=task, label=page_home_text:
                self.update_task(t, checked, label)
        )

        # Riscar

        page_home_text2 = QLabel(task.date.toString("dd/MM"))
        page_home_text2.setObjectName("page_home_text2")

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

        frame_home_layout = QHBoxLayout(frame_home)
        frame_home_layout.addWidget(page_home_button)
        frame_home_layout.addWidget(page_home_text)
        frame_home_layout.addStretch()
        frame_home_layout.addWidget(page_home_text2)
        frame_home_layout.addWidget(options_button)

        layout.addWidget(frame_home)

    # Home Side
    # //////////////////////////////////////////////////////////
    def create_page_home_side(self):
        self.page_home_side = QFrame()
        self.page_home_side.setMinimumWidth(300)
        self.page_home_side.setMaximumWidth(360)
        self.page_home_side.setObjectName("page_home_side")

        # Page Home Calendar
        self.create_page_home_calendar()

        # Page Home Statistics / Day's Summary
        self.create_home_statistics()

        self.page_home_side_layout = QVBoxLayout(self.page_home_side)
        self.page_home_side_layout.setSpacing(15)
        self.page_home_side_layout.setAlignment(Qt.AlignTop)
        self.page_home_side_layout.addWidget(self.frame_home_calendar)
        self.page_home_side_layout.addWidget(self.frame_home_statistics)
        # self.page_home_side_layout.addStretch()

    # Calendar
    def create_page_home_calendar(self):
        self.calendar = QCalendarWidget()
        self.calendar.setObjectName("calendar")
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendar.setGridVisible(False)
        self.calendar.setNavigationBarVisible(True)
        self.calendar.setMinimumSize(260, 240)
        self.calendar.setMaximumSize(360, 260)

        # Sabado e Domingo
        fmt = QTextCharFormat()
        fmt.setForeground(QColor("#FF7A7A"))
        self.calendar.setWeekdayTextFormat(Qt.Saturday, fmt)
        self.calendar.setWeekdayTextFormat(Qt.Sunday, fmt)

        # Destacar Dia de Hoje
        today = QTextCharFormat()
        today.setBackground(QColor("pink"))
        today.setForeground(QColor("white"))
        self.calendar.setDateTextFormat(QDate.currentDate(), today)


        self.frame_home_calendar = QFrame()
        self.frame_home_calendar.setObjectName("frame_home_calendar")
        self.frame_home_calendar.setMinimumSize(280, 220)
        self.frame_home_calendar.setMaximumSize(380, 280)

        # Sombra no Frame
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 100))
        self.frame_home_calendar.setGraphicsEffect(shadow)

        frame_home_layout = QVBoxLayout(self.frame_home_calendar)
        frame_home_layout.addWidget(self.calendar)


        # Botoes
        self.prev = self.calendar.findChild(QToolButton, "qt_calendar_prevmonth")
        self.next = self.calendar.findChild(QToolButton, "qt_calendar_nextmonth")

        self.prev.setIconSize(QSize(18, 18))
        self.next.setIconSize(QSize(18, 18))

    # Statistics
    def create_home_statistics(self):
        self.frame_home_statistics = QFrame()
        self.frame_home_statistics.setObjectName("frame_home_statistics")
        self.frame_home_statistics.setMinimumSize(280, 120)
        self.frame_home_statistics.setMaximumSize(380, 180)
        self.statistics_layout = QVBoxLayout(self.frame_home_statistics)

        self.refresh_statistics()

    # Refresh
    # //////////////////////////////////////////////////////////
    def refresh(self):
        # Refresh Cards
        self.clear_layout(self.today_tasks_layout)
        self.clear_layout(self.upcoming_tasks_layout)

        self.today_tasks_text.setText(
            f"🔥 Tarefas de Hoje - {len(self.task_manager.get_today_tasks())}"
        )

        self.upcoming_tasks_text.setText(
            f"⏰ Próximas Tarefas - {len(self.task_manager.get_upcoming_tasks(limit=4))}"
        )

        self.load_tasks()

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)

            if item.widget():
                item.widget().deleteLater()

            elif item.layout():
                self.clear_layout(item.layout())

    # Refresh Statistics
    # //////////////////////////////////////////////////////////
    def refresh_statistics(self):
        while self.statistics_layout.count():
            item = self.statistics_layout.takeAt(0)

            if item.widget():
                item.widget().deleteLater()

        stats = self.task_manager.get_task_statistics(self.task_manager.get_today_tasks())

        self.page_home_statistics_text = QLabel(f"📊 Estatisticas do Dia")
        self.page_home_statistics_text.setObjectName("page_home_statistics_text")

        self.page_home_statistics_all = QLabel(f"🎯📝📋⫶☰ Total de Tarefas - {stats["total"]}")
        self.page_home_statistics_all.setObjectName("page_home_statistics_all")
        self.page_home_statistics_all.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.page_home_statistics_completed = QLabel(f"✅ Concluidas - {stats["completed"]}")
        self.page_home_statistics_completed.setObjectName("page_home_statistics_completed")
        self.page_home_statistics_completed.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.page_home_statistics_pending = QLabel(f"🎯📝📋⫶☰ Pendentes - {stats["incomplete"]}")
        self.page_home_statistics_pending.setObjectName("page_home_statistics_pending")
        self.page_home_statistics_pending.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.statistics_layout.addWidget(self.page_home_statistics_text)
        self.statistics_layout.addWidget(self.page_home_statistics_all)
        self.statistics_layout.addWidget(self.page_home_statistics_completed)
        self.statistics_layout.addWidget(self.page_home_statistics_pending)

    # Update Task
    # //////////////////////////////////////////////////////////
    def update_task(self, task, checked, label):
        task.is_completed = checked

        if checked:
            label.setStyleSheet(
                "text-decoration: line-through;"
            )
        else:
            label.setStyleSheet("")

        for history_task in self.history_manager.tasks:
            if history_task.id == task.id:
                history_task.is_completed = checked
                break

        self.refresh_statistics()
        self.task_manager.database.save_tasks(self.task_manager.tasks)
        self.history_manager.database.save_history(self.history_manager.tasks)

    # Clicked Options Button
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

        delete_action = menu.addAction("🗑️  Excluir")
        delete_action.triggered.connect(
            lambda: self.confirm_delete_task(task_id)
        )

        pos = options_button.mapToGlobal(
            options_button.rect().bottomLeft()
        )

        menu.exec(pos)

    # Clicked Delete Task
    def confirm_delete_task(self, task_id):
        reply = QMessageBox.question(
            self,
            "Excluir tarefa",
            "Tem certeza que deseja excluir esta tarefa?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.history_manager.mark_as_deleted(task_id)
            self.task_manager.remove_task(task_id)
            self.refresh_statistics()
            self.refresh()

    # Apply Theme
    # //////////////////////////////////////////////////////////
    def apply_theme(self):
        self.styles = THEMES[self.settings["theme"]]

        self.setStyleSheet(self.styles["page_home"])

        if self.settings["theme"] == "dark":
            self.prev.setIcon(QIcon("icons/chevron_left_white.svg"))
            self.next.setIcon(QIcon("icons/chevron_right_white.svg"))
        else:
            self.prev.setIcon(QIcon("icons/chevron_left_black.svg"))
            self.next.setIcon(QIcon("icons/chevron_right_black.svg"))

        # Cards
        self.refresh()