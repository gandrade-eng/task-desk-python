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
        self.form.setObjectName("form")
        self.form.setMinimumWidth(500)
        self.form.setMinimumHeight(500)
        self.form_layout = QVBoxLayout(self.form)
        self.form_layout.setContentsMargins(50, 50, 50, 50)
        self.form_layout.setSpacing(15)



        self.title_input_label = QLabel("📝 Título")
        self.title_input_label.setObjectName("title_input_label")

        self.title_input = QLineEdit()
        self.title_input.setObjectName("title_input")
        self.title_input.setFixedHeight(38)
        self.title_input.setPlaceholderText("Título da tarefa")



        self.date_input_label = QLabel("📅 Data")
        self.date_input_label.setObjectName("date_input_label")
        self.date_input = QDateEdit()
        self.date_input.setObjectName("date_input")
        self.date_input.setFixedHeight(38)
        self.date_input.setCalendarPopup(True)

        self.date_layout = QVBoxLayout()
        self.date_layout.addWidget(self.date_input_label)
        self.date_layout.addWidget(self.date_input)


        self.time_input_label = QLabel("⏰ Hora")
        self.time_input_label.setObjectName("time_input_label")
        self.time_input = QTimeEdit()
        self.time_input.setObjectName("time_input")
        self.time_input.setFixedHeight(38)

        self.time_layout = QVBoxLayout()
        self.time_layout.addWidget(self.time_input_label)
        self.time_layout.addWidget(self.time_input)


        self.date_time_layout = QHBoxLayout()
        self.date_time_layout.addLayout(self.date_layout)
        self.date_time_layout.addLayout(self.time_layout)


        self.description_input_label = QLabel("Descrição")
        self.description_input_label.setObjectName("description_input_label")
        
        self.description_input = QTextEdit()
        self.description_input.setObjectName("description_input")
        self.description_input.setFixedHeight(120)
        self.description_input.setPlaceholderText("Descrição (opcional)")



        self.form_layout.addWidget(self.title_input_label)
        self.form_layout.addWidget(self.title_input)
        self.form_layout.addLayout(self.date_time_layout)
        self.form_layout.addWidget(self.description_input_label)
        self.form_layout.addWidget(self.description_input)


        self.options_send = QPushButton("Adicionar")
        self.options_send.setObjectName("options_send")
        self.options_send.setMinimumHeight(100)
        self.options_send.setMinimumWidth(100)


        self.options_cancel = QPushButton("Cancelar")
        self.options_cancel.setObjectName("options_cancel")
        self.options_cancel.setMinimumHeight(100)
        self.options_cancel.setMinimumWidth(100)


        self.options_layout = QHBoxLayout()
        self.options_layout.setContentsMargins(50, 50, 50, 50)
        # self.options_layout.addStretch()
        self.options_layout.addWidget(self.options_send)
        self.options_layout.addWidget(self.options_cancel)
        


        self.page_addtask_layout = QVBoxLayout(self)
        self.page_addtask_layout.addWidget(self.form)
        self.page_addtask_layout.addLayout(self.options_layout)

        self.apply_theme()

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

    # Apply Theme
    # //////////////////////////////////////////////////////////
    def apply_theme(self):
        self.styles = THEMES[self.settings["theme"]]

        self.setStyleSheet(self.styles["add_task"])

        # Cards
        # self.refresh()