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
            #header_text {
                border: none; 
                color: black
            }
            #header_button {
                border: 1px solid black;
                border-radius: 10px;
                color: black
            }
            #today_tasks_text {
                color: black
            }
            #upcoming_tasks_text {
                color: black
            }
            #page_home_side {
                border: none
            }
            #frame_home_calendar {
                border: 1px solid black;
                border-radius: 10px
            }
            #frame_home_statistics {
                border: 1px solid black;
                border-radius: 10px
            }
            #page_home_statistics_text {
                border: none;
                color: black
            }
            #page_home_statistics_all {
                border: 1px solid black;
                border-radius: 10px;
                color: black
            }
            #page_home_statistics_completed {
                border: 1px solid black;
                border-radius: 10px;
                color: black
            }
            #page_home_statistics_pending {
                border: 1px solid black;
                border-radius: 10px;
                color: black
            }
            #frame_home {
                border: 1px solid black;
                border-radius: 10px;
            }
            QCheckBox#page_home_button::indicator {
                width: 18px;
                height: 18px;
                border-radius: 8px;
                border: 2px solid #D1D5DB;
                background: white;
            }
            QCheckBox#page_home_button::indicator:hover {
                border: 2px solid #3B82F6;
            }
            QCheckBox#page_home_button::indicator:checked {
                background: black;
                border: 2px solid black;
            }
            #page_home_text {
                border: none;
                color: black
            }
            #page_home_text2 {
                border: none;
                color: black
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
        "title_notification_settings": "font-size: 18px; font-weight: bold; color: #FFFFFF;",

        "page_home": """
            #header_text {
                border: none;
                color: #F9FAFB;
            }
            #header_button {
                border: 1px solid #4B5563;
                border-radius: 10px;
                background-color: #374151;
                color: #F9FAFB;
            }
            #header_button:hover {
                background-color: #4B5563;
            }
            #today_tasks_text {
                color: #F9FAFB;
            }
            #upcoming_tasks_text {
                color: #F9FAFB;
            }
            #page_home_side {
                border: none;
            }
            #frame_home_calendar {
                border: 1px solid #4B5563;
                border-radius: 10px;
                background-color: #1F2937;
            }
            #frame_home_statistics {
                border: 1px solid #4B5563;
                border-radius: 10px;
                background-color: #1F2937;
            }
            #page_home_statistics_text {
                border: none;
                color: #F9FAFB;
            }
            #page_home_statistics_all {
                border: 1px solid #4B5563;
                border-radius: 10px;
                background-color: #111827;
                color: #F9FAFB;
            }
            #page_home_statistics_completed {
                border: 1px solid #4B5563;
                border-radius: 10px;
                background-color: #111827;
                color: #F9FAFB;
            }
            #page_home_statistics_pending {
                border: 1px solid #4B5563;
                border-radius: 10px;
                background-color: #111827;
                color: #F9FAFB;
            }
            #frame_home {
                border: 1px solid #4B5563;
                border-radius: 10px;
                background-color: #1F2937;
            }
            QCheckBox#page_home_button::indicator {
                width: 18px;
                height: 18px;
                border-radius: 8px;
                border: 2px solid #6B7280;
                background: #111827;
            }
            QCheckBox#page_home_button::indicator:hover {
                border: 2px solid #60A5FA;
            }
            QCheckBox#page_home_button::indicator:checked {
                background: #60A5FA;
                border: 2px solid #60A5FA;
            }
            #page_home_text {
                border: none;
                color: #F9FAFB;
            }
            #page_home_text2 {
                border: none;
                color: #D1D5DB;
            }
        """,
    }
}