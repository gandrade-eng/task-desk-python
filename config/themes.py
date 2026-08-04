THEMES = {
    "light": {
        "left_menu": "background-color: #F3F4F6",
        "left_menu_top_frame": "background-color: #E9ECEF",
        "line": "background-color: #E9ECEF; border: none",
        "main_menu":"background-color: #FFFFFF",


        "page_settings_theme_title": "font-size: 18px; font-weight: bold; color: black;",
        "page_settings_language_title": "font-size: 18px; font-weight: bold; color: black;",
        "title_notification_settings": "font-size: 18px; font-weight: bold; color: black;",




        "page_home": """
            QFrame {
                border: 1px solid black;
                border-radius: 10px;
            }

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
            """,

        "tasks_page":"""
            QProgressBar {
                border: 1px solid #888;
                border-radius: 5px;
                text-align: center;
                height: 18px;
            }

            QProgressBar::chunk {
                background-color: #4CAF50;
                border-radius: 4px;
            }

            QLabel {
                color: black
            }
        """
    },






    "dark": {
        "left_menu": "background-color: #1E1E1E",
        "left_menu_top_frame": "background-color: #252526",
        "line": "background-color: #333333; border: none",
        "main_menu": "background-color: #121212",


        "page_settings_theme_title": "font-size: 18px; font-weight: bold; color: #FFFFFF;",
        "page_settings_language_title": "font-size: 18px; font-weight: bold; color: #FFFFFF;",
        "title_notification_settings": "font-size: 18px; font-weight: bold; color: #FFFFFF;"
    }
}