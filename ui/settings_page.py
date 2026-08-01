
from config.settings import THEMES, LANGUAGES

from PySide6.QtCore import QSize, Signal
from PySide6.QtGui import Qt, QIcon
from PySide6.QtWidgets import (
    QMainWindow, QFrame, QHBoxLayout, 
    QVBoxLayout, QSpacerItem, QSizePolicy, 
    QLabel, QWidget, QStackedWidget, 
    QApplication, QPushButton, QCheckBox,
    QButtonGroup, QRadioButton
)

class SettingsPage(QWidget):
    def __init__(self, settings):
        super().__init__()

        self.settings = settings
        self.create_page_settings()

    def create_page_settings(self):
        # label_page_home.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page_settings_layout = QVBoxLayout(self)
        self.page_settings_layout.setContentsMargins(50, 50, 50, 50)

        # Page Settings Theme
        self.page_settings_theme = QLabel()
        self.page_settings_theme.setStyleSheet("background-color: #D1D5DB; border-radius: 10px;")

        self.page_settings_theme_title = QLabel(LANGUAGES[self.settings["language"]]["theme"])
        self.page_settings_theme_title.setStyleSheet(THEMES[self.settings["theme"]]["page_settings_theme_title"])

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
        self.create_settings_language()

        # Page Settings Notification
        self.page_settings_notifications = QLabel()
        self.page_settings_notifications.setStyleSheet("background-color: #D1D5DB; border-radius: 10px;")
        
        self.page_settings_notifications_title = QLabel(LANGUAGES[self.settings["language"]]["notifications"])
        self.page_settings_notifications_title.setStyleSheet(THEMES[self.settings["theme"]]["page_settings_notifications_title"])

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

    def create_settings_language(self):
        self.page_settings_language = QLabel()
        self.page_settings_language.setStyleSheet("background-color: #D1D5DB; border-radius: 10px;")

        self.page_settings_language_title = QLabel(LANGUAGES[self.settings["language"]]["language"])
        self.page_settings_language_title.setStyleSheet(THEMES[self.settings["theme"]]["page_settings_language_title"])

        self.page_settings_language_options_layout = QVBoxLayout()
        self.language_group = QButtonGroup()

        self.pt_radio = QRadioButton("Português")
        self.pt_radio.setStyleSheet("""
            QRadioButton::indicator {
                width: 18px;
                height: 18px;
                border-radius: 8px;
                border: 2px solid #D1D5DB;
                background: white;
            }

            QRadioButton::indicator:hover {
                border: 2px solid #3B82F6;
            }

            QRadioButton::indicator:checked {
                background: black;
                border: 2px solid black;
            }
            """)
        self.en_radio = QRadioButton("English")
        self.en_radio.setStyleSheet("""
            QRadioButton::indicator {
                width: 18px;
                height: 18px;
                border-radius: 8px;
                border: 2px solid #D1D5DB;
                background: white;
            }

            QRadioButton::indicator:hover {
                border: 2px solid #3B82F6;
            }

            QRadioButton::indicator:checked {
                background: black;
                border: 2px solid black;
            }
            """)
        self.es_radio = QRadioButton("Español")
        self.es_radio.setStyleSheet("""
            QRadioButton::indicator {
                width: 18px;
                height: 18px;
                border-radius: 8px;
                border: 2px solid #D1D5DB;
                background: white;
            }

            QRadioButton::indicator:hover {
                border: 2px solid #3B82F6;
            }

            QRadioButton::indicator:checked {
                background: black;
                border: 2px solid black;
            }
            """)

        self.language_group.addButton(self.pt_radio)
        self.language_group.addButton(self.en_radio)
        self.language_group.addButton(self.es_radio)

        self.en_radio.setChecked(True)

        self.page_settings_language_options_layout.addWidget(self.pt_radio)
        self.page_settings_language_options_layout.addWidget(self.en_radio)
        self.page_settings_language_options_layout.addWidget(self.es_radio)

        self.page_settings_language_layout = QVBoxLayout(self.page_settings_language)
        self.page_settings_language_layout.setContentsMargins(20, 20, 20, 20)
        self.page_settings_language_layout.addWidget(self.page_settings_language_title)
        self.page_settings_language_layout.addStretch()
        self.page_settings_language_layout.addLayout(self.page_settings_language_options_layout)