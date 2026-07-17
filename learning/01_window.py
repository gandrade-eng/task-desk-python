from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import sys

# MainWindow herda QMainWindow
class MainWindow(QMainWindow):
    # Construtor da Classe
    def __init__(self):
        super().__init__()

        # self equivale a this (this.setTitle("exemplo"))
        # show mostra a janela
        self.show()

# QApplication gerencia a aplicação
app = QApplication(sys.argv)
# Cria a Janela
window = MainWindow()
# Cria o loop, experando eventos
sys.exit(app.exec())