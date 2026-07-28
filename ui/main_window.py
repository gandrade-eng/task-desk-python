# A janela principal.
# Ela mostra:

# lista de tarefas
# botão adicionar
# botão remover
# botão editar
# botão configurações

# É praticamente a tela principal.

from settings import THEMES, theme, LANGUAGES, language

from PySide6.QtCore import QSize
from PySide6.QtGui import Qt, QIcon
from PySide6.QtWidgets import (
    QMainWindow, QFrame, QHBoxLayout, 
    QVBoxLayout, QSpacerItem, QSizePolicy, 
    QLabel, QWidget, QStackedWidget, 
    QApplication, QPushButton, QCheckBox
)

# from ..services.database import loadSettings

import sys


# self.pages_text.setStyleSheet("font: 700 9pt 'Segoe UI'")
# self.pages.setStyleSheet("font-size: 12pt; color: #1F2430")
# self.top_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)


# Fundo principal	Branco	#FFFFFF
# Fundo secundário	Cinza muito claro	#F7F8FA
# Barra lateral	Cinza claro	#F3F4F6
# Cards	Branco	#FFFFFF
# Hover	Cinza	#E9ECEF
# Borda	Cinza claro	#DCDFE4

# Principal	#1F2937
# Secundário	#6B7280
# Desabilitado	#9CA3AF

# border-left: 5px solid #44475a;


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

# Primary Window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

        # self.Settings = loadSettings

        self.set_active_menu(self.left_menu_home_button)
        self.left_menu_home_button.clicked.connect(self.home_clicked)
        self.left_menu_tasks_button.clicked.connect(self.tasks_clicked)
        self.left_menu_settings_button.clicked.connect(self.settings_clicked)

        self.show()

    # Setup Ui
    # //////////////////////////////////////////////////////////
    def setup_ui(self):
        # Main Window Configuration
        self.setObjectName("MainWindow")
        self.setWindowTitle("TaskDesk")
        self.resize(750, 650)
        self.setMinimumSize(750,650)

        # Central Frame
        self.central_frame = QFrame()

        # Main Layout
        # //////////////////////////////////////////////////////////
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Left Menu 
        # //////////////////////////////////////////////////////////
        self.create_left_menu()
        
        # Line
        # //////////////////////////////////////////////////////////
        self.line = QFrame()
        self.line.setFixedWidth(2)
        self.line.setStyleSheet(THEMES[theme]["line"])

        # Main Menu
        # //////////////////////////////////////////////////////////
        self.create_main_menu()

        # Pages
        # //////////////////////////////////////////////////////////
        # Page Home
        self.page_home = QWidget()
        layout_page_home = QVBoxLayout()
        label_page_home = QLabel("Hello World")
        label_page_home.setStyleSheet("color: black;")
        label_page_home.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_page_home.addWidget(label_page_home)
        self.page_home.setLayout(layout_page_home)

        # Page Tasks
        self.page_tasks = QWidget()

        # Page Settings
        self.create_page_settings()

        # Stacked Pages
        self.pages = QStackedWidget()
        self.pages.addWidget(self.page_home)
        self.pages.addWidget(self.page_tasks)
        self.pages.addWidget(self.page_settings)

        # Add in Window
        # //////////////////////////////////////////////////////////
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.line)
        self.main_layout.addWidget(self.main_menu)

        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_version_label)

        self.left_menu_top_layout.addWidget(self.left_menu_home_button)
        self.left_menu_top_layout.addWidget(self.left_menu_tasks_button)

        self.left_menu_bottom_layout.addWidget(self.left_menu_settings_button)

        self.main_menu_layout.addWidget(self.pages)


        self.setCentralWidget(self.central_frame)

    # Create Left Menu
    # //////////////////////////////////////////////////////////
    def create_left_menu(self):
        self.left_menu = QFrame()
        self.left_menu.setMinimumWidth(75)
        self.left_menu.setMaximumWidth(75)
        self.left_menu.setStyleSheet(THEMES[theme]["left_menu"])


        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)


        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        # self.left_menu_top_frame.setStyleSheet(THEMES[theme]["left_menu_top_frame"])


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

    # Create Main Menu
    # //////////////////////////////////////////////////////////
    def create_main_menu(self):
        self.main_menu = QFrame()
        self.main_menu.setStyleSheet(THEMES[theme]["main_menu"])

        self.main_menu_layout = QHBoxLayout(self.main_menu)
        self.main_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.main_menu_layout.setSpacing(0)

    def create_page_home(self):
        print()

    def create_page_tasks(self):
        print()

    def create_page_settings(self):
        self.page_settings_layout = QVBoxLayout()
        self.page_settings_layout.setContentsMargins(50, 50, 50, 50)

        self.page_settings = QWidget()
        self.page_settings.setLayout(self.page_settings_layout)

        # Page Settings Theme
        self.page_settings_theme = QLabel()
        self.page_settings_theme.setStyleSheet("background-color: #D1D5DB; border-radius: 10px;")

        self.page_settings_theme_title = QLabel(LANGUAGES[language]["theme"])
        self.page_settings_theme_title.setStyleSheet(THEMES[theme]["page_settings_theme_title"])

        self.page_settings_all_themes = QHBoxLayout()

        self.light_theme_button = QPushButton("☀ Claro")
        self.light_theme_button.setFixedSize(120, 50)
        self.light_theme_button.setStyleSheet("""
            QPushButton {
                background-color: #FFFFFF;
                color: black;
                border: 2px solid #D1D5DB;
                border-radius: 10px;
            }

            QPushButton:hover {
                background-color: #E5E7EB;
            }
        """)

        self.dark_theme_button = QPushButton("🌙 Escuro")
        self.dark_theme_button.setFixedSize(120, 50)
        self.dark_theme_button.setStyleSheet("""
            QPushButton {
                background-color: #1F2937;
                color: white;
                border: 2px solid #111827;
                border-radius: 10px;
            }

            QPushButton:hover {
                background-color: #374151;
            }
        """)

        self.page_settings_all_themes.addWidget(self.light_theme_button)
        self.page_settings_all_themes.setSpacing(10)
        self.page_settings_all_themes.addWidget(self.dark_theme_button)

        self.page_settings_theme_layout = QVBoxLayout(self.page_settings_theme)
        self.page_settings_theme_layout.setContentsMargins(20, 20, 20, 20)
        self.page_settings_theme_layout.addWidget(self.page_settings_theme_title)
        self.page_settings_theme_layout.addStretch()
        self.page_settings_theme_layout.addLayout(self.page_settings_all_themes)


        # Page Settings Language
        self.page_settings_language = QLabel()
        self.page_settings_language.setStyleSheet("background-color: #D1D5DB; border-radius: 10px;")

        self.page_settings_language_title = QLabel(LANGUAGES[language]["language"])
        self.page_settings_language_title.setStyleSheet(THEMES[theme]["page_settings_language_title"])

        self.page_settings_language_layout = QVBoxLayout(self.page_settings_language)
        self.page_settings_language_layout.setContentsMargins(20, 20, 20, 20)
        self.page_settings_language_layout.addWidget(self.page_settings_language_title)
        self.page_settings_language_layout.addStretch()
        # self.page_settings_language_layout.addLayout(self.page_settings_all_themes)

        # Page Settings Notification
        self.page_settings_notifications = QLabel()
        self.page_settings_notifications.setStyleSheet("background-color: #D1D5DB; border-radius: 10px;")
        
        self.page_settings_notifications_title = QLabel(LANGUAGES[language]["notifications"])
        self.page_settings_notifications_title.setStyleSheet(THEMES[theme]["page_settings_notifications_title"])

        self.page_settings_notifications_checkbox = QCheckBox("Ativar notificações")

        self.page_settings_notifications_checkbox.setStyleSheet("color: black; font-size: 14px;")
        
        self.page_settings_notifications_layout = QVBoxLayout(self.page_settings_notifications)
        self.page_settings_notifications_layout.setContentsMargins(20, 20, 20, 20)
        self.page_settings_notifications_layout.addWidget(self.page_settings_notifications_title)
        self.page_settings_notifications_layout.addStretch()
        self.page_settings_notifications_layout.addWidget(self.page_settings_notifications_checkbox)


        self.page_settings_layout.addWidget(self.page_settings_theme)
        self.page_settings_layout.addWidget(self.page_settings_language)
        self.page_settings_layout.addWidget(self.page_settings_notifications)

    # //////////////////////////////////////////////////////////
    def set_active_menu(self, active_button):
        buttons = [
            self.left_menu_home_button,
            self.left_menu_tasks_button,
            self.left_menu_settings_button,
        ]
    
        for button in buttons:
            button.set_active(button == active_button)

    def home_clicked(self):
        self.set_active_menu(self.left_menu_home_button)
        self.pages.setCurrentWidget(self.page_home)
    
    def tasks_clicked(self):
        self.set_active_menu(self.left_menu_tasks_button)
        self.pages.setCurrentWidget(self.page_tasks)
    
    def settings_clicked(self):
        self.set_active_menu(self.left_menu_settings_button)
        self.pages.setCurrentWidget(self.page_settings)

def main_loop():
    # QApplication gerencia a aplicação
    app = QApplication(sys.argv)
    # Cria a Janela
    window = MainWindow()
    # Cria o loop, experando eventos
    sys.exit(app.exec())

if __name__ == "__main__":
    main_loop()