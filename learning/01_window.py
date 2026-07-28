from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from homeButton import homeButton

import sys

# MainWindow herda QMainWindow
class MainWindow(QMainWindow):
    # Construtor da Classe
    def __init__(self):
        super().__init__()

        # setup ui vai estar numa classe que tem esse nome
        # self.ui = UI_MainWindow()
        #self.ui.setup_ui(self)
        self.setup_ui()

        # animation
        self.left_menu_home_button.clicked.connect(self.home_button)

        self.set_active_menu(self.left_menu_home_button)
        self.left_menu_home_button.clicked.connect(self.home_clicked)
        self.left_menu_tasks_button.clicked.connect(self.tasks_clicked)
        self.left_menu_settings_button.clicked.connect(self.settings_clicked)

        # self equivale a this (this.setTitle("exemplo"))
        # show mostra a janela
        self.show()
    
    def home_clicked(self):
        self.set_active_menu(self.left_menu_home_button)
        self.pages.setCurrentWidget(self.page_1)
        self.home_button()

    def tasks_clicked(self):
        self.set_active_menu(self.left_menu_tasks_button)
        self.pages.setCurrentWidget(self.page_2)

    def settings_clicked(self):
        self.set_active_menu(self.left_menu_settings_button)
        self.pages.setCurrentWidget(self.page_3)

    def set_active_menu(self, active_button):
        buttons = [
            self.left_menu_home_button,
            self.left_menu_tasks_button,
            self.left_menu_settings_button,
        ]

        for button in buttons:
            button.set_active(button == active_button)

    # Animation
    def home_button(self):
        # self.ui.left_menu
        menu_width = self.left_menu.width()
    
        width = 50
        if menu_width == 50:
            width = 200
    
        self.animation = QPropertyAnimation(self.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(300)
        # .setEasingCurve (QEasingCurve.[animacao]) anima
        self.animation.start()
    
    def setup_ui(self):
        self.setObjectName("MainWindow")

        # self.setWindowIcon()
        self.setWindowTitle("TaskDesk")
        self.resize(1200, 720)
        self.setMinimumSize(960,540)

        self.central_frame = QFrame()

        # Left Menu
        # //////////////////////////////////////////////////////////
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #CDC9C9")
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)

        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)

        # Left Menu - Top Frame
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        self.left_menu_top_frame.setStyleSheet("background-color: red")

        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_top_layout.setSpacing(0)

        # Left Menu - Spacer
        self.left_menu_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # Left Menu - Bottom Frame
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(50)
        self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")
        self.left_menu_bottom_frame.setStyleSheet("#left_menu_bottom_frame { background-color: red; }")
        # self.left_menu_bottom_frame.setStyleSheet("background-color: red")

        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_bottom_layout.setSpacing(0)

        # Left Menu - Label Version
        self.left_menu_version_label = QLabel("v1.0.0")
        self.left_menu_version_label.setStyleSheet("color: #1F2430")
        self.left_menu_version_label.setAlignment(Qt.AlignCenter)
        self.left_menu_version_label.setMinimumHeight(30)
        self.left_menu_version_label.setMaximumHeight(30)

        # Left Menu - Buttons
        self.left_menu_home_button = homeButton(
            # btn_hover = "red",
            is_activate = True,
            text = "Home"
        )
        self.left_menu_tasks_button = homeButton(
            is_activate = False,
            text = "Tasks"
        )
        self.left_menu_settings_button = homeButton(
            is_activate = False,
            text = "Settings"
        )

        # Main Menu
        # //////////////////////////////////////////////////////////
        self.main_menu = QFrame()
        self.main_menu.setStyleSheet("background-color: #FAFAFC")

        # Top Bar
        # //////////////////////////////////////////////////////////
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet("background-color: #6C4CF1")

        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10, 0, 10, 0)
        self.top_bar_layout.setSpacing(0)

        # Top Bar - Left Label
        self.top_label_left = QLabel("Testando")

        # Top Bar - Spacer
        self.top_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Top Bar - Right Label
        self.top_label_right = QLabel("Teste")
        self.top_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

        # Page
        # //////////////////////////////////////////////////////////
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #1F2430")

        self.pages_text = QLabel("Teste")
        self.pages_text.setStyleSheet("font: 700 9pt 'Segoe UI'")

        # Page_1
        self.page_1 = QWidget()
        layout_page1 = QVBoxLayout()
        label_page1 = QLabel("Hello World")
        label_page1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_page1.addWidget(label_page1)
        self.page_1.setLayout(layout_page1)

        # Page_2
        self.page_2 = QWidget()
        layout_page2 = QVBoxLayout()
        label_page2 = QLabel("World")
        label_page2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_page2.addWidget(label_page2)
        self.page_2.setLayout(layout_page2)

        # Page_3
        self.page_3 = QWidget()

        self.pages.addWidget(self.page_1)
        self.pages.addWidget(self.page_2)
        self.pages.addWidget(self.page_3)

        # Main Layout
        # //////////////////////////////////////////////////////////
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Content Layout
        # //////////////////////////////////////////////////////////
        self.content_layout = QVBoxLayout(self.main_menu)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # Add in Main Layout
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.main_menu)

        # Add in Content Layout
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)

        # Add in Top Bar
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_label_right)

        # Add in Left Menu
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_version_label)

        # Add in Left Menu - Top
        self.left_menu_top_layout.addWidget(self.left_menu_home_button)
        self.left_menu_top_layout.addWidget(self.left_menu_tasks_button)

        # Add in Left Menu - Bottom
        self.left_menu_bottom_layout.addWidget(self.left_menu_settings_button)

        # Add in Page

        self.setCentralWidget(self.central_frame)

# QApplication gerencia a aplicação
app = QApplication(sys.argv)
# Cria a Janela
window = MainWindow()
# Cria o loop, experando eventos
sys.exit(app.exec())