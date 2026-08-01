
from config.settings import THEMES, LANGUAGES

from PySide6.QtCore import QSize, Signal
from PySide6.QtGui import Qt, QIcon
from PySide6.QtWidgets import (
    QMainWindow, QFrame, QHBoxLayout, 
    QVBoxLayout, QSpacerItem, QSizePolicy, 
    QLabel, QWidget, QStackedWidget, 
    QApplication, QPushButton, QCheckBox
)

class HomePage(QWidget):
    addtask_clicked = Signal()

    def __init__(self, settings):
        super().__init__()

        self.settings = settings
        self.create_page_home()

        self.page_home_main_header_button.clicked.connect(self.addtask_clicked.emit)

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

    def create_page_home_main(self):
        self.page_home_main_layout = QVBoxLayout()

        self.page_home_main_header_text = QLabel("Tarefas")
        self.page_home_main_header_text.setStyleSheet("border: none ; color: black")
        self.page_home_main_header_button = QPushButton("Adicionar")
        self.page_home_main_header_button.setStyleSheet("border: 1px solid black; border-radius: 10px; color: black")

        self.page_home_main_header_layout = QHBoxLayout()
        self.page_home_main_header_layout.addWidget(self.page_home_main_header_text)
        self.page_home_main_header_layout.addWidget(self.page_home_main_header_button)
        self.page_home_main_layout.addLayout(self.page_home_main_header_layout)

        self.page_home_main_body_today_task_text = QLabel(f"Tarefas de Hoje - {2}")
        self.page_home_main_body_today_task_text.setStyleSheet("color: black")
        self.page_home_main_layout.addWidget(self.page_home_main_body_today_task_text)
        for i in range(2):
            self.create_home_main_body_today_task(i)

        self.page_home_main_body_upcoming_tasks_text = QLabel(f"Proximas Tarefas - {3}")
        self.page_home_main_body_upcoming_tasks_text.setStyleSheet("color: black")
        self.page_home_main_layout.addWidget(self.page_home_main_body_upcoming_tasks_text)
        for i in range(3):
            self.create_home_main_body_upcoming_tasks(i)

        self.page_home_main_layout.addStretch()
            
    def create_home_main_body_today_task(self, i):
        frame_home = QFrame()
        frame_home.setMaximumHeight(80)
        frame_home.setMaximumWidth(300)
        frame_home.setStyleSheet("""
            QFrame {
                border: 1px solid black;
                border-radius: 10px;
            }
            """)
        frame_home_layout = QHBoxLayout(frame_home)

        page_home_button = QCheckBox()
        page_home_button.setStyleSheet("""
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border-radius: 8px;
                border: 2px solid #D1D5DB;
                background: white;
            }

            QCheckBox::indicator:hover {
                border: 2px solid #3B82F6;
            }

            QCheckBox::indicator:checked {
                background: black;
                border: 2px solid black;
            }
            """)
        page_home_text = QLabel(f"Prova {i} \nHora: 10:{i}")
        page_home_text.setStyleSheet("border: none; color: black")

        # Riscar
        # font = page_home_text.font()
        # font.setStrikeOut(True)
        # page_home_text.setFont(font)
        
        page_home_text2 = QLabel(f"{i}/2")
        page_home_text2.setStyleSheet("border: none; color: black")

        frame_home_layout.addWidget(page_home_button)
        frame_home_layout.addWidget(page_home_text)
        frame_home_layout.addStretch()
        frame_home_layout.addWidget(page_home_text2)

        self.page_home_main_layout.addWidget(frame_home)

    def create_home_main_body_upcoming_tasks(self,i):
        frame_home = QFrame()
        frame_home.setMaximumHeight(80)
        frame_home.setMaximumWidth(300)
        frame_home.setStyleSheet("""
            QFrame {
                border: 1px solid black;
                border-radius: 10px;
            }
            """)
        frame_home_layout = QHBoxLayout(frame_home)

        page_home_button = QCheckBox()
        page_home_button.setStyleSheet("""
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border-radius: 8px;
                border: 2px solid #D1D5DB;
                background: white;
            }

            QCheckBox::indicator:hover {
                border: 2px solid #3B82F6;
            }

            QCheckBox::indicator:checked {
                background: black;
                border: 2px solid black;
            }
            """)
        page_home_text = QLabel(f"Prova {i} \nHora: 10:{i}")
        page_home_text.setStyleSheet("border: none; color: black")

        # Riscar
        # font = page_home_text.font()
        # font.setStrikeOut(True)
        # page_home_text.setFont(font)
        
        page_home_text2 = QLabel(f"{i}/2")
        page_home_text2.setStyleSheet("border: none; color: black")

        frame_home_layout.addWidget(page_home_button)
        frame_home_layout.addWidget(page_home_text)
        frame_home_layout.addStretch()
        frame_home_layout.addWidget(page_home_text2)

        self.page_home_main_layout.addWidget(frame_home)

    def create_page_home_side(self):
        self.page_home_side = QFrame()
        self.page_home_side_layout = QVBoxLayout(self.page_home_side)
        self.page_home_side.setStyleSheet("border: none")
        # Page Home Statistics / Day's Summary
        self.create_page_home_statistics()
        self.page_home_side_layout.addWidget(self.frame_home_statistics)
        self.page_home_side_layout.addStretch()

    def create_page_home_statistics(self):
        self.frame_home_statistics = QFrame()
        self.frame_home_statistics.setStyleSheet("border: 1px solid black; border-radius: 10px")
        frame_home_layout = QVBoxLayout(self.frame_home_statistics)

        self.page_home_statistics_text = QLabel(f"Estatisticas do Dia")
        self.page_home_statistics_text.setStyleSheet("border: none ; color: black")
        self.page_home_statistics_all = QLabel(f"🎯📝📋⫶☰ Total de Tarefas - {20}")
        self.page_home_statistics_all.setStyleSheet("border: 1px solid black; border-radius: 10px; color: black")
        self.page_home_statistics_all.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page_home_statistics_completed = QLabel(f"✅ Concluidas - {10}")
        self.page_home_statistics_completed.setStyleSheet("border: 1px solid black; border-radius: 10px; color: black")
        self.page_home_statistics_completed.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page_home_statistics_pending = QLabel(f"🎯📝📋⫶☰ Pendentes - {10}")
        self.page_home_statistics_pending.setStyleSheet("border: 1px solid black; border-radius: 10px; color: black")
        self.page_home_statistics_pending.setAlignment(Qt.AlignmentFlag.AlignCenter)

        frame_home_layout.addWidget(self.page_home_statistics_text)
        frame_home_layout.addWidget(self.page_home_statistics_all)
        frame_home_layout.addWidget(self.page_home_statistics_completed)
        frame_home_layout.addWidget(self.page_home_statistics_pending)