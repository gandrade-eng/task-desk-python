# external imports
from PySide6.QtCore import QSize, Signal, QDate, QTime
from PySide6.QtGui import Qt, QIcon
from PySide6.QtWidgets import (
    QMainWindow, QFrame, QHBoxLayout, 
    QVBoxLayout, QSpacerItem, QSizePolicy, 
    QLabel, QWidget, QStackedWidget, 
    QApplication, QPushButton, QCheckBox,
    QFormLayout, QLineEdit, QDateEdit,
    QTimeEdit, QTextEdit, QMessageBox
)
# internal imports
from models import Task
from config import THEMES, LANGUAGES

# title = self.title_input.text()
# task = Task (id = database.next_id(), title = title, ...)

class AddTask(QWidget):
    task_created = Signal(str, QDate, QTime, str)

    def __init__(self, settings):
        super().__init__()

        self.settings = settings
        self.create_page_addtask()

        self.options_send.clicked.connect(self.on_send_clicked)
    
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

    def on_send_clicked(self):
        if not self.title_input.text().strip():
            QMessageBox.warning(self, "Erro", "Digite um título.")
            return

        self.task_created.emit(
            self.title_input.text(),
            self.date_input.date(),
            self.time_input.time(),
            self.description_input.toPlainText()
        )