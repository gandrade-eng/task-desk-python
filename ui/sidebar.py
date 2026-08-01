
from config.settings import THEMES, LANGUAGES

from PySide6.QtCore import QSize, Signal
from PySide6.QtGui import Qt, QIcon
from PySide6.QtWidgets import (
    QMainWindow, QFrame, QHBoxLayout, 
    QVBoxLayout, QSpacerItem, QSizePolicy, 
    QLabel, QWidget, QStackedWidget, 
    QApplication, QPushButton, QCheckBox
)

class customButton(QPushButton):
    def __init__(
        self,
        height=70,
        minimum_width = 500,
        text_color="#1F2937",
        icon_path="",
        icon_color="red",
        btn_color="#F3F4F6",
        btn_hover="#E9ECEF",
        btn_pressed="#282a36",
        is_activate=False
    ):
        super().__init__()

        if icon_path:
            icon = QIcon(icon_path)

            self.setIcon(icon)
            self.setIconSize(QSize(50, 50))

        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        self.minimum_width = minimum_width
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_activate = is_activate

        self.set_style()


    def set_active(self, is_activate):
        self.is_activate = is_activate
        self.set_style()


    def set_style(self):

        style = f"""
        QPushButton {{
            background-color: {self.btn_color};
            border: none;
            border-radius: 10px;
        }}

        QPushButton:hover {{
            background-color: {self.btn_hover};
        }}

        QPushButton:pressed {{
            background-color: {self.btn_pressed};
        }}
        """

        if self.is_activate:
            style += """
            QPushButton {
                background-color: #D1D5DB;
                border: 1px solid #C7CCD4;
            }
            """

        self.setStyleSheet(style)

class SideBar(QWidget):
    home_clicked = Signal()
    tasks_clicked = Signal()
    settings_clicked = Signal()

    def __init__(self, settings):
        super().__init__()

        self.settings = settings
        self.create_left_menu()

        self.left_menu_home_button.clicked.connect(self.home_clicked.emit)
        self.left_menu_tasks_button.clicked.connect(self.tasks_clicked.emit)
        self.left_menu_settings_button.clicked.connect(self.settings_clicked.emit)

    def create_left_menu(self):
        self.left_menu = QFrame()
        self.left_menu.setMinimumWidth(75)
        self.left_menu.setMaximumWidth(75)
        self.left_menu.setStyleSheet(THEMES[self.settings["theme"]]["left_menu"])


        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)


        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        # self.left_menu_top_frame.setStyleSheet(THEMES[self.settings["theme"]]["left_menu_top_frame"])


        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(5, 5, 5, 5)
        self.left_menu_top_layout.setSpacing(10)


        self.left_menu_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)


        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(50)
        # self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")
        # self.left_menu_bottom_frame.setStyleSheet("#left_menu_bottom_frame { background-color: red; }")
        # self.left_menu_bottom_frame.setStyleSheet("background-color: red")
        

        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(5, 5, 5, 5)
        self.left_menu_bottom_layout.setSpacing(0)

        
        self.left_menu_version_label = QLabel("v1.0.0")
        self.left_menu_version_label.setStyleSheet("color: #1F2430")
        self.left_menu_version_label.setAlignment(Qt.AlignCenter)
        self.left_menu_version_label.setMinimumHeight(30)
        self.left_menu_version_label.setMaximumHeight(30)


        self.left_menu_home_button = customButton(
            icon_path = "../task-desk-python/icons/home.svg",
            is_activate = True
        )

        self.left_menu_tasks_button = customButton(
            icon_path = "../task-desk-python/icons/task.svg",
            is_activate = False,
        )

        self.left_menu_settings_button = customButton(
            icon_path = "../task-desk-python/icons/settings.svg",
            is_activate = False,
        )

        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_version_label)

        # Add in Left Menu Top
        self.left_menu_top_layout.addWidget(self.left_menu_home_button)
        self.left_menu_top_layout.addWidget(self.left_menu_tasks_button)

        # Add in Left Menu Bottom
        self.left_menu_bottom_layout.addWidget(self.left_menu_settings_button)



        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.left_menu)