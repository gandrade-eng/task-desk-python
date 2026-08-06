PAGE_SETTINGS = """
    #page_settings_theme,
    #page_settings_language,
    #page_settings_notifications {
        background-color: #FFFFFF;

        border: 1px solid #F3D6E0;
        border-radius: 14px;
    }


    #page_settings_theme_title,
    #language_title,
    #notifications_title {
        color: #1F2937;

        font-size: 18px;
        font-weight: 600;
    }


    /* ---------- Theme Buttons ---------- */

    QPushButton#light_theme_button,
    QPushButton#dark_theme_button,
    QPushButton#pink_theme_button {
        border-radius: 10px;

        padding: 8px 14px;

        font-size: 14px;
        font-weight: 600;
    }


    QPushButton#light_theme_button {
        background-color: #FFFFFF;
        color: #1F2937;

        border: 1px solid #F3D6E0;
    }
    QPushButton#light_theme_button:hover {
        background-color: #FFF0F6;
        border: 1px solid #EC4899;
    }
    QPushButton#light_theme_button:pressed {
        background-color: #FCE7F3;
    }


    QPushButton#dark_theme_button {
        background-color: #1F2937;
        color: white;

        border: 1px solid #111827;
    }
    QPushButton#dark_theme_button:hover {
        background-color: #374151;
        border: 1px solid #EC4899;
    }
    QPushButton#dark_theme_button:pressed {
        background-color: #111827;
    }

    
    QPushButton#pink_theme_button {
        background-color: #EC4899;
        color: white;

        border: 1px solid #EC4899;
    }
    QPushButton#pink_theme_button:hover {
        background-color: #DB2777;
        border: 1px solid #DB2777;
    }
    QPushButton#pink_theme_button:pressed {
        background-color: #BE185D;
    }


    /* ---------- Idiomas ---------- */

    QRadioButton#language_pt,
    QRadioButton#language_en,
    QRadioButton#language_es {
        color: #1F2937;

        font-size: 14px;
    }


    QRadioButton#language_pt::indicator,
    QRadioButton#language_en::indicator,
    QRadioButton#language_es::indicator {
        width: 18px;
        height: 18px;

        border-radius: 9px;

        border: 2px solid #F3D6E0;
        background: white;
    }


    QRadioButton#language_pt::indicator:hover,
    QRadioButton#language_en::indicator:hover,
    QRadioButton#language_es::indicator:hover {
        border: 2px solid #EC4899;
    }


    QRadioButton#language_pt::indicator:checked,
    QRadioButton#language_en::indicator:checked,
    QRadioButton#language_es::indicator:checked {
        background: #EC4899;
        border: 2px solid #EC4899;
    }


    /* ---------- Notificações ---------- */

    #notifications_checkbox {
        color: #1F2937;
        font-size: 14px;
    }


    QCheckBox#notifications_checkbox::indicator {
        width: 18px;
        height: 18px;

        border-radius: 6px;

        border: 2px solid #F3D6E0;
        background: white;
    }


    QCheckBox#notifications_checkbox::indicator:hover {
        border: 2px solid #EC4899;
    }


    QCheckBox#notifications_checkbox::indicator:checked {
        background: #EC4899;
        border: 2px solid #EC4899;
    }
"""