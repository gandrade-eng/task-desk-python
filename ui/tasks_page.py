
from config.settings import THEMES, LANGUAGES

from PySide6.QtCore import QSize, Signal
from PySide6.QtGui import Qt, QIcon
from PySide6.QtWidgets import (
    QMainWindow, QFrame, QHBoxLayout, 
    QVBoxLayout, QSpacerItem, QSizePolicy, 
    QLabel, QWidget, QStackedWidget, 
    QApplication, QPushButton, QCheckBox
)

# Estatísticas
# Mostrar:
# Total: 20
# Concluídas: 14
# Pendentes: 6
# 70% concluídas

class TasksPage(QWidget):
    def __init__(self, settings):
        super().__init__()

        self.settings = settings
        self.create_page_tasks()

    def create_page_tasks(self):
        self.page_tasks = QVBoxLayout(self)

        self.page_tasks_statistics = QHBoxLayout()

        # Titulo
        # Pesquisa
        # Filtros

        # Criar/Editar/Excluir
        # Todas as Tarefas

        # Taxa de conclusão
        # ████████░░ 82%
        # 82% das tarefas criadas foram concluídas
        self.overall_progress = QLabel()

        # Tarefas criadas:
        # Janeiro    32
        # Fevereiro  45
        # Março      27
        # Abril      51
        self.history_statistics = QLabel()

        # Total
        # 245 tarefas
        # Concluídas 180
        # Pendentes 40
        # Atrasadas 25
        self.general_status = QLabel()