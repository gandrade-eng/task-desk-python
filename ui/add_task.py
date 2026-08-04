from config import THEMES, LANGUAGES

from PySide6.QtCore import QSize, Signal
from PySide6.QtGui import Qt, QIcon
from PySide6.QtWidgets import (
    QMainWindow, QFrame, QHBoxLayout, 
    QVBoxLayout, QSpacerItem, QSizePolicy, 
    QLabel, QWidget, QStackedWidget, 
    QApplication, QPushButton, QCheckBox,
    QFormLayout, QLineEdit, QDateEdit,
    QTimeEdit, QTextEdit
)

# title = self.title_input.text()
# task = Task (id = database.next_id(), title = title, ...)

class AddTask(QWidget):
    def __init__(self, settings):
        super().__init__()

        self.settings = settings
        self.create_page_addtask()
    
    def create_page_addtask(self):
        self.form = QFrame()
        self.form.setStyleSheet("color: black")
        self.form.setMinimumWidth(500)
        self.form.setMinimumHeight(500)
        self.form_layout = QFormLayout(self.form)
        self.form_layout.setContentsMargins(50, 50, 50, 50)

        self.title_input = QLineEdit()
        self.date_input = QDateEdit()
        self.time_input = QTimeEdit()
        self.description_input = QTextEdit()

        self.form_layout.addRow("Título:", self.title_input)
        self.form_layout.addRow("Data:", self.date_input)
        self.form_layout.addRow("Hora:", self.time_input)
        self.form_layout.addRow("Descrição:", self.description_input)

        self.options_send = QPushButton("Adicionar")
        self.options_send.setStyleSheet("color: black; border-radius: 10px; border: 1px solid black;")
        self.options_send.setMinimumHeight(100)
        self.options_send.setMinimumWidth(100)
        self.options_cancel = QPushButton("Cancelar")
        self.options_cancel.setStyleSheet("color: black; border-radius: 10px; border: 1px solid black;")
        self.options_cancel.setMinimumHeight(100)
        self.options_cancel.setMinimumWidth(100)
        self.options_layout = QHBoxLayout()
        self.options_layout.setContentsMargins(50, 50, 50, 50)
        self.options_layout.addStretch()
        self.options_layout.addWidget(self.options_send)
        self.options_layout.addWidget(self.options_cancel)
        


        self.page_addtask_layout = QVBoxLayout(self)
        self.page_addtask_layout.addWidget(self.form)
        self.page_addtask_layout.addLayout(self.options_layout)