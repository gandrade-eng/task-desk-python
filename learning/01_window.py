from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import sys

# MainWindow herda QMainWindow
class MainWindow(QMainWindow):
    # Construtor da Classe
    def __init__(self):
        super().__init__()

        self.setup_ui()

        # self equivale a this (this.setTitle("exemplo"))
        # show mostra a janela
        self.show()
    
    def setup_ui(self):
        self.setObjectName("MainWindow")

        self.setWindowTitle("TaskDesk")
        self.resize(1200, 720)
        self.setMinimumSize(960,540)

        self.central_frame = QFrame()

        self.leftMenu = QFrame()
        self.leftMenu.setStyleSheet("background-color: #CDC9C9")
        self.leftMenu.setMaximumWidth(65)

        self.mainMenu = QFrame()
        self.mainMenu.setStyleSheet("background-color: #FAFAFC")

        self.topBar = QFrame()
        self.topBar.setMinimumHeight(30)
        self.topBar.setMaximumHeight(30)
        self.topBar.setStyleSheet("background-color: #6C4CF1")

        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.contentLayout = QVBoxLayout(self.mainMenu)
        self.contentLayout.setContentsMargins(0, 0, 0, 0)
        self.contentLayout.setSpacing(0)

        self.main_layout.addWidget(self.leftMenu)
        self.main_layout.addWidget(self.mainMenu)

        self.contentLayout.addWidget(self.topBar)

        self.setCentralWidget(self.central_frame)

# QApplication gerencia a aplicação
app = QApplication(sys.argv)
# Cria a Janela
window = MainWindow()
# Cria o loop, experando eventos
sys.exit(app.exec())