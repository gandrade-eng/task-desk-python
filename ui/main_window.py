# external imports
# from PySide6.QtCore import QSize
# from PySide6.QtGui import Qt, QIcon
from PySide6.QtWidgets import (
    QMainWindow, QFrame, QHBoxLayout, 
    QStackedWidget, 
)

# internal imports
from ui import (
    SideBar, SettingsPage, HomePage,
    TasksPage, AddTask
)
from config import THEMES, LANGUAGES, SettingsManager
from services import TaskManager, Database, HistoryManager

# self.pages_text.setStyleSheet("font: 700 9pt 'Segoe UI'")
# self.pages.setStyleSheet("font-size: 12pt; color: #1F2430")
# self.top_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

# Primary Window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Loading the File
        # tasks = loadTasks()

        self.settings = SettingsManager.load_settings()

        self.database = Database()
        self.history_manager = HistoryManager(Database())
        self.task_manager = TaskManager(Database(), HistoryManager(Database()))

        self.setup_ui()
        # self.apply_settings()
        # self.load_task()
        # self.update_statistics()

        self.set_active_menu(self.home_clicked)

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
        self.setCentralWidget(self.central_frame)

        # Central Frame Layout
        self.central_frame_layout = QHBoxLayout(self.central_frame)
        self.central_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.central_frame_layout.setSpacing(0)

        # Create Side Bar
        # //////////////////////////////////////////////////////////
        self.side_bar = SideBar(self.settings)

        self.side_bar.home_page_requested.connect(self.home_clicked)
        self.side_bar.tasks_page_requested.connect(self.tasks_clicked)
        self.side_bar.settings_page_requested.connect(self.settings_clicked)
        
        # Line
        self.line = QFrame()
        self.line.setObjectName("line")
        self.line.setFixedWidth(2)
        
        # Main Menu
        self.create_main_menu()

        # Page Home
        # //////////////////////////////////////////////////////////
        self.page_home = HomePage(self.settings, self.task_manager, self.history_manager)

        self.page_home.add_task_page_requested.connect(self.addtask_clicked)

        # Page Tasks
        # //////////////////////////////////////////////////////////
        self.page_tasks = TasksPage(self.settings, self.task_manager, self.history_manager)

        self.page_tasks.add_task_page_requested.connect(self.addtask_clicked)

        # Page Settings
        # //////////////////////////////////////////////////////////
        self.page_settings = SettingsPage(self.settings)

        self.page_settings.theme_light_clicked.connect(self.theme_light_clicked)
        self.page_settings.theme_dark_clicked.connect(self.theme_dark_clicked)
        self.page_settings.theme_pink_clicked.connect(self.theme_pink_clicked)

        # Page Add Task
        # //////////////////////////////////////////////////////////
        self.page_addtask = AddTask(self.settings)

        self.page_addtask.task_created.connect(self.handle_task_created)

        # Stacked Pages
        self.pages = QStackedWidget()
        self.pages.addWidget(self.page_home)
        self.pages.addWidget(self.page_tasks)
        self.pages.addWidget(self.page_settings)

        self.pages.addWidget(self.page_addtask)

        # Add in Main
        self.central_frame_layout.addWidget(self.side_bar)
        self.central_frame_layout.addWidget(self.line)
        self.central_frame_layout.addWidget(self.main_menu)

        # Add in Main Menu
        self.main_menu_layout.addWidget(self.pages)

        self.apply_theme()
    

    # Create Main Menu
    # //////////////////////////////////////////////////////////
    def create_main_menu(self):
        self.main_menu = QFrame()
        self.main_menu.setObjectName("main_menu")

        self.main_menu_layout = QHBoxLayout(self.main_menu)
        self.main_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.main_menu_layout.setSpacing(0)

    # //////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////
    def set_active_menu(self, active_button):
        buttons = [
            self.side_bar.left_menu_home_button,
            self.side_bar.left_menu_tasks_button,
            self.side_bar.left_menu_settings_button,
        ]
    
        for button in buttons:
            button.set_active(button == active_button)

    def home_clicked(self):
        self.set_active_menu(self.side_bar.left_menu_home_button)
        self.pages.setCurrentWidget(self.page_home)
    
    def tasks_clicked(self):
        self.set_active_menu(self.side_bar.left_menu_tasks_button)
        self.pages.setCurrentWidget(self.page_tasks)

    def addtask_clicked(self):
        self.pages.setCurrentWidget(self.page_addtask)

    # Clicked Settings
    # //////////////////////////////////////////////////////////
    def settings_clicked(self):
        self.set_active_menu(self.side_bar.left_menu_settings_button)
        self.pages.setCurrentWidget(self.page_settings)

    def theme_light_clicked(self):
        self.settings["theme"] = "light"

        SettingsManager.save_settings(self.settings)

        self.apply_theme()

    def theme_dark_clicked(self):
        self.settings["theme"] = "dark"

        SettingsManager.save_settings(self.settings)

        self.apply_theme()

    def theme_pink_clicked(self):
        self.settings["theme"] = "pink"
        
        SettingsManager.save_settings(self.settings)

        self.apply_theme()

    # Clicked Add Task
    # //////////////////////////////////////////////////////////
    def handle_task_created(self, title, date, time, description):
        new_task = self.task_manager.add_task(title, date, time, description, False)

        self.history_manager.add_history(new_task)

        # self.page_tasks.refresh()
        self.page_home.refresh()

        self.pages.setCurrentWidget(self.page_home)

    # //////////////////////////////////////////////////////////
    def cancel_task_created():
        ...
        # self.pages.setCurrentWidget(self.page_home)

    # Apply Theme
    # //////////////////////////////////////////////////////////
    def apply_theme(self):
        self.setStyleSheet(THEMES[self.settings["theme"]]["main_window"])
        self.side_bar.apply_theme()
        self.page_home.apply_theme()
        self.page_settings.apply_theme()
        self.page_addtask.apply_theme()