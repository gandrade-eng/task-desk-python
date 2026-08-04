from config import THEMES, LANGUAGES

from PySide6.QtCore import Signal
from PySide6.QtGui import Qt
from PySide6.QtWidgets import (
    QFrame, QHBoxLayout, QVBoxLayout, 
    QLabel, QWidget, QPushButton, QCheckBox,
    QCalendarWidget
)

class HomePage(QWidget):
    add_task_page_requested = Signal()

    def __init__(self, settings, task_manager):
        super().__init__()

        self.settings = settings
        self.task_manager = task_manager

        self.create_page_home()

        self.page_home_main_header_button.clicked.connect(self.add_task_page_requested.emit)

    # //////////////////////////////////////////////////////////
    def create_page_home(self):
        self.page_home_layout = QHBoxLayout(self)
        self.page_home_layout.setContentsMargins(10,10,10,10)

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

    # //////////////////////////////////////////////////////////
    def create_page_home_main(self):
        self.page_home_main_layout = QVBoxLayout()

        self.page_home_main_header_text = QLabel("Tarefas")
        self.page_home_main_header_text.setStyleSheet("border: none ; color: black")
        self.page_home_main_header_button = QPushButton("➕ Adicionar")
        self.page_home_main_header_button.setStyleSheet("border: 1px solid black; border-radius: 10px; color: black")

        self.page_home_main_header_layout = QHBoxLayout()
        self.page_home_main_header_layout.addWidget(self.page_home_main_header_text)
        self.page_home_main_header_layout.addWidget(self.page_home_main_header_button)
        self.page_home_main_layout.addLayout(self.page_home_main_header_layout)


        # MUDAR DPS POR FAVOR
        self.today_tasks_text = QLabel(f"🔥 Tarefas de Hoje - {len(self.task_manager.get_today_tasks())}")
        self.today_tasks_text.setStyleSheet("color: black")
        self.page_home_main_layout.addWidget(self.today_tasks_text)

        self.today_tasks_layout = QVBoxLayout()
        self.page_home_main_layout.addLayout(self.today_tasks_layout)

        # MUDAR DPS POR FAVOR
        self.upcoming_tasks_text = QLabel(f"⏰ Proximas Tarefas - {len(self.task_manager.get_upcoming_tasks(None))}")
        self.upcoming_tasks_text.setStyleSheet("color: black")
        self.page_home_main_layout.addWidget(self.upcoming_tasks_text)

        self.upcoming_tasks_layout = QVBoxLayout()
        self.page_home_main_layout.addLayout(self.upcoming_tasks_layout)

        self.load_tasks()

        self.page_home_main_layout.addStretch()

    # 
    def load_tasks(self):
        today_tasks = self.task_manager.get_today_tasks()

        for task in today_tasks:
            self.create_task_card(task, self.today_tasks_layout)

        upcoming_tasks = self.task_manager.get_upcoming_tasks(3)

        for task in upcoming_tasks:
            self.create_task_card(task, self.upcoming_tasks_layout)

    # 
    def create_task_card(self, task, layout):
        frame_home = QFrame()
        frame_home.setMaximumHeight(80)
        frame_home.setMaximumWidth(300)
        frame_home.setStyleSheet(THEMES[self.settings["theme"]]["page_home"])

        frame_home_layout = QHBoxLayout(frame_home)

        page_home_button = QCheckBox()
        page_home_button.setStyleSheet(THEMES[self.settings["theme"]]["page_home"])

        page_home_text = QLabel(
            f"{task.title}\nHora: {task.time.toString('HH:mm')}"
        )
        page_home_text.setStyleSheet("border: none; color: black")

         # Riscar
        font = page_home_text.font()
        font.setStrikeOut(True)
        page_home_text.setFont(font)

        page_home_text2 = QLabel(task.date.toString("dd/MM"))
        page_home_text2.setStyleSheet("border: none; color: black")

        frame_home_layout.addWidget(page_home_button)
        frame_home_layout.addWidget(page_home_text)
        frame_home_layout.addStretch()
        frame_home_layout.addWidget(page_home_text2)

        layout.addWidget(frame_home)

    # 
    # //////////////////////////////////////////////////////////
    def create_page_home_side(self):
        self.page_home_side = QFrame()
        self.page_home_side_layout = QVBoxLayout(self.page_home_side)
        self.page_home_side.setStyleSheet("border: none")

        today_tasks = self.task_manager.get_today_tasks()

        # Page Home Calendar
        self.create_page_home_calendar()

        # Page Home Statistics / Day's Summary
        self.create_home_statistics(today_tasks)

        self.page_home_side_layout.addWidget(self.frame_home_calendar)
        self.page_home_side_layout.addWidget(self.frame_home_statistics)
        self.page_home_side_layout.addStretch()

    def create_page_home_calendar(self):
        # from PySide6.QtCore import Slot
        # self.calendar.clicked.connect(self.show_tasks_by_date)

        # def show_tasks_by_date(self, date):
        #     selected_date = date.toString("yyyy-MM-dd")
        #     tasks = [
        #         task for task in self.task_manager.get_tasks()
        #         if task.date == selected_date
        #     ]
        #     for task in tasks:
        #         self.create_task_card(task)

        self.calendar = QCalendarWidget()

        self.frame_home_calendar = QFrame()
        self.frame_home_calendar.setStyleSheet("border: 1px solid black; border-radius: 10px")

        frame_home_layout = QVBoxLayout(self.frame_home_calendar)
        frame_home_layout.addWidget(self.calendar)

    def create_home_statistics(self, today_tasks):
        stats = self.task_manager.get_task_statistics(today_tasks)

        self.frame_home_statistics = QFrame()
        self.frame_home_statistics.setStyleSheet("border: 1px solid black; border-radius: 10px")
        frame_home_layout = QVBoxLayout(self.frame_home_statistics)

        self.page_home_statistics_text = QLabel(f"📊 Estatisticas do Dia")
        self.page_home_statistics_text.setStyleSheet("border: none ; color: black")
        self.page_home_statistics_all = QLabel(f"🎯📝📋⫶☰ Total de Tarefas - {stats["total"]}")
        self.page_home_statistics_all.setStyleSheet("border: 1px solid black; border-radius: 10px; color: black")
        self.page_home_statistics_all.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page_home_statistics_completed = QLabel(f"✅ Concluidas - {stats["completed"]}")
        self.page_home_statistics_completed.setStyleSheet("border: 1px solid black; border-radius: 10px; color: black")
        self.page_home_statistics_completed.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page_home_statistics_pending = QLabel(f"🎯📝📋⫶☰ Pendentes - {stats["incomplete"]}")
        self.page_home_statistics_pending.setStyleSheet("border: 1px solid black; border-radius: 10px; color: black")
        self.page_home_statistics_pending.setAlignment(Qt.AlignmentFlag.AlignCenter)

        frame_home_layout.addWidget(self.page_home_statistics_text)
        frame_home_layout.addWidget(self.page_home_statistics_all)
        frame_home_layout.addWidget(self.page_home_statistics_completed)
        frame_home_layout.addWidget(self.page_home_statistics_pending)

    # Refresh
    # //////////////////////////////////////////////////////////
    def refresh(self):
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