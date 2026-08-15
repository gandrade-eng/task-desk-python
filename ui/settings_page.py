from config import THEMES, LANGUAGES

from PySide6.QtCore import QSize, Signal
from PySide6.QtGui import Qt, QIcon
from PySide6.QtWidgets import (
    QMainWindow, QFrame, QHBoxLayout, 
    QVBoxLayout, QSpacerItem, QSizePolicy, 
    QLabel, QWidget, QStackedWidget, 
    QApplication, QPushButton, QCheckBox,
    QButtonGroup, QRadioButton
)

# label_page_home.setAlignment(Qt.AlignmentFlag.AlignCenter)

class SettingsPage(QWidget):
    theme_light_clicked = Signal()
    theme_dark_clicked = Signal()
    theme_pink_clicked = Signal()

    data_export_clicked = Signal()
    data_import_clicked = Signal()

    def __init__(self, settings):
        super().__init__()

        self.settings = settings
        self.create_page_settings()

    def create_page_settings(self):
        self.page_settings_layout = QVBoxLayout(self)
        self.page_settings_layout.setContentsMargins(50, 50, 50, 50)

        # Page Settings Theme
        self.create_settings_theme()

        # Page Settings Language
        self.create_settings_language()

        # Page Settings Notification
        self.create_settings_notification()

        # Page Settings Data
        self.create_settings_data()

        # Add in Layout
        self.page_settings_layout.addWidget(self.page_settings_theme)
        self.page_settings_layout.addWidget(self.page_settings_language)
        self.page_settings_layout.addWidget(self.page_settings_notifications)
        self.page_settings_layout.addWidget(self.settings_data)

        self.apply_theme()

    # //////////////////////////////////////////////////////////
    def create_settings_theme(self):
        self.page_settings_theme = QFrame()
        self.page_settings_theme.setObjectName("page_settings_theme")

        self.page_settings_theme_title = QLabel(LANGUAGES[self.settings["language"]]["theme"])
        self.page_settings_theme_title.setObjectName("page_settings_theme_title")

        self.page_settings_all_themes = QHBoxLayout()

        self.light_theme_button = QPushButton("☀ Claro")
        self.light_theme_button.setObjectName("light_theme_button")
        self.light_theme_button.setFixedSize(120, 50)
        self.light_theme_button.clicked.connect(self.theme_light_clicked.emit)

        self.dark_theme_button = QPushButton("🌙 Escuro")
        self.dark_theme_button.setObjectName("dark_theme_button")
        self.dark_theme_button.setFixedSize(120, 50)
        self.dark_theme_button.clicked.connect(self.theme_dark_clicked.emit)

        self.pink_theme_button = QPushButton("🌸 Rosa")
        self.pink_theme_button.setObjectName("pink_theme_button")
        self.pink_theme_button.setFixedSize(120, 50)
        self.pink_theme_button.clicked.connect(self.theme_pink_clicked.emit)

        self.page_settings_all_themes.addWidget(self.light_theme_button)
        self.page_settings_all_themes.setSpacing(10)
        self.page_settings_all_themes.addWidget(self.dark_theme_button)
        self.page_settings_all_themes.setSpacing(10)
        self.page_settings_all_themes.addWidget(self.pink_theme_button)

        self.page_settings_theme_layout = QVBoxLayout(self.page_settings_theme)
        self.page_settings_theme_layout.setContentsMargins(20, 20, 20, 20)
        self.page_settings_theme_layout.addWidget(self.page_settings_theme_title)
        self.page_settings_theme_layout.addStretch()
        self.page_settings_theme_layout.addLayout(self.page_settings_all_themes)

    # //////////////////////////////////////////////////////////
    def create_settings_language(self):
        self.page_settings_language = QFrame()
        self.page_settings_language.setObjectName("page_settings_language")

        self.language_title = QLabel(LANGUAGES[self.settings["language"]]["language"])
        self.language_title.setObjectName("language_title")
        
        self.page_settings_language_options_layout = QHBoxLayout()
        self.language_group = QButtonGroup()

        self.language_pt = QRadioButton("Português")
        self.language_pt.setObjectName("language_pt")

        language_en = QRadioButton("English")
        language_en.setObjectName("language_en")
        
        language_es = QRadioButton("Español")
        language_es.setObjectName("language_es")

        self.language_group.addButton(self.language_pt)
        self.language_group.addButton(language_en)
        self.language_group.addButton(language_es)

        language_en.setChecked(True)

        self.page_settings_language_options_layout.addWidget(self.language_pt)
        self.page_settings_language_options_layout.addWidget(language_en)
        self.page_settings_language_options_layout.addWidget(language_es)

        self.page_settings_language_layout = QVBoxLayout(self.page_settings_language)
        self.page_settings_language_layout.setContentsMargins(20, 20, 20, 20)
        self.page_settings_language_layout.addWidget(self.language_title)
        self.page_settings_language_layout.addLayout(self.page_settings_language_options_layout)
        self.page_settings_language_layout.addStretch()

    # //////////////////////////////////////////////////////////
    def create_settings_notification(self):
        self.page_settings_notifications = QFrame()
        self.page_settings_notifications.setObjectName("page_settings_notifications")
        
        self.notifications_title = QLabel(LANGUAGES[self.settings["language"]]["notifications"])
        self.notifications_title.setObjectName("notifications_title")

        self.notifications_checkbox = QCheckBox("Ativar notificações")
        self.notifications_checkbox.setObjectName("notifications_checkbox")
        
        self.page_settings_notifications_layout = QVBoxLayout(self.page_settings_notifications)
        self.page_settings_notifications_layout.setContentsMargins(20, 20, 20, 20)
        self.page_settings_notifications_layout.addWidget(self.notifications_title)
        self.page_settings_notifications_layout.addStretch()
        self.page_settings_notifications_layout.addWidget(self.notifications_checkbox)

    # //////////////////////////////////////////////////////////
    def create_settings_data(self):
        # [Exportar tarefas] 
        # [Importar tarefas]
        self.settings_data = QFrame()
        self.settings_data.setObjectName("settings_data")

        self.data_title = QLabel("💾 Dados")
        self.data_title.setObjectName("data_title")

        self.data_button_export = QPushButton("Exportar Tarefas")
        self.data_button_export.setObjectName("data_button_export")
        self.data_button_export.setFixedSize(120, 50)
        self.data_button_export.clicked.connect(self.data_export_clicked.emit)

        self.data_button_import = QPushButton("Importar Tarefas")
        self.data_button_import.setObjectName("data_button_import")
        self.data_button_import.setFixedSize(120, 50)
        self.data_button_import.clicked.connect(self.data_import_clicked.emit)

        self.data_layout = QHBoxLayout()
        self.data_layout.addWidget(self.data_button_export)
        self.data_layout.addWidget(self.data_button_import)

        self.settings_data_layout = QVBoxLayout(self.settings_data)
        self.settings_data_layout.setContentsMargins(20, 20, 20, 20)
        self.settings_data_layout.addWidget(self.data_title)
        self.settings_data_layout.addStretch()
        self.settings_data_layout.addLayout(self.data_layout)

    # Apply Theme
    # //////////////////////////////////////////////////////////
    def apply_theme(self):
        self.styles = THEMES[self.settings["theme"]]

        self.setStyleSheet(self.styles["page_settings"])

        # Cards
        # self.refresh()