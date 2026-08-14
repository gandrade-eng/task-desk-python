from config import THEMES, LANGUAGES

from PySide6.QtCore import QSize, Signal
from PySide6.QtGui import Qt, QIcon
from PySide6.QtWidgets import (
    QMainWindow, QFrame, QHBoxLayout, 
    QVBoxLayout, QSpacerItem, QSizePolicy, 
    QLabel, QWidget, QStackedWidget, 
    QApplication, QPushButton, QCheckBox,
    QProgressBar
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

        # Titulo
        # Pesquisa
        # Filtros

        # Criar/Editar/Excluir
        # Todas as Tarefas
        self.create_tasks_list()

        self.create_tasks_statistics()

        # self.page_tasks.addWidget()
        self.page_tasks.addLayout(self.page_tasks_statistics)

    # Tasks List
    # //////////////////////////////////////////////////////////
    def create_tasks_list(self):
        self.page_tasls_list = QVBoxLayout()

        text_one = QLabel("Todas as Tarefas")


    # Tasks Statistics
    # //////////////////////////////////////////////////////////
    def create_tasks_statistics(self):
        self.page_tasks_statistics = QHBoxLayout()

        self.create_overall_progress()

        self.create_history_statistics()

        self.create_general_status()

        self.page_tasks_statistics.addLayout(self.overall_progress)
        self.page_tasks_statistics.addLayout(self.history_statistics)
        self.page_tasks_statistics.addLayout(self.general_status)

    # Overall Progress
    def create_overall_progress(self):
        # Taxa de conclusão
        # ████████░░ 82%
        # 82% das tarefas criadas foram concluídas
        stats = self.history_manager.get_task_completion_percentage(self.history_manager.get_tasks())

        self.overall_progress = QVBoxLayout()

        # percentage = 0
        # if stats["total"] > 0:
        #     percentage = int(stats["completed"] / stats["total"] * 100)
        # self.completion_bar.setValue(percentage)
        # self.completion_label.setText(
        #     f"{percentage}% das tarefas criadas foram concluídas."
        # )

        text_one = QLabel("Taxa de conclusão")
        text_one.setStyleSheet(THEMES[self.settings["theme"]]["tasks_page"])

        completion_bar = QProgressBar()
        completion_bar.setMinimum(0)
        completion_bar.setMaximum(100)
        completion_bar.setValue(stats)
        completion_bar.setTextVisible(True)
        completion_bar.setFormat("%p%")
        completion_bar.setStyleSheet(THEMES[self.settings["theme"]]["tasks_page"])

        text_two = QLabel("82% das tarefas criadas foram concluídas")
        text_two.setStyleSheet(THEMES[self.settings["theme"]]["tasks_page"])

        self.overall_progress.addWidget(text_one)
        self.overall_progress.addWidget(completion_bar)
        self.overall_progress.addWidget(text_two)

    def create_history_statistics(self):
        # Tarefas criadas:
        # Janeiro    32
        # Fevereiro  45
        # Março      27
        # Abril      51

        # history

        self.history_statistics = QHBoxLayout()

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
            month_label.setMinimumSize(150, 50)
            month_label.setStyleSheet("color: black; border-radius: 5px; border: 1px solid black;")

            if i < 6:
                self.history_statistics_left.addWidget(month_label)
            else:
                self.history_statistics_right.addWidget(month_label)

        self.history_statistics.addLayout(self.history_statistics_left)
        self.history_statistics.addLayout(self.history_statistics_right)

    def create_general_status(self):
        # Total
        # 245 tarefas
        # Concluídas 180
        # Pendentes 40
        # Atrasadas 25

        self.general_status = QVBoxLayout()
