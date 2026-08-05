PAGE_SETTINGS = """
    #page_settings_theme,
    #page_settings_language,
    #page_settings_notifications {
        background-color: #1F2937;

        border: 1px solid #374151;
        border-radius: 14px;
    }
    #page_settings_theme_title,
    #language_title,
    #notifications_title {
        color: #F9FAFB;

        font-size: 18px;
        font-weight: 600;
    }

    /* ---------- Theme Buttons ---------- */
    QPushButton#light_theme_button,
    QPushButton#dark_theme_button {
        border-radius: 10px;

        padding: 8px 14px;

        font-size: 14px;
        font-weight: 600;
    }
    QPushButton#light_theme_button {
        background-color: #F3F4F6;
        color: #111827;

        border: 1px solid #D1D5DB;
    }
    QPushButton#light_theme_button:hover {
        border: 1px solid #60A5FA;
        background-color: #FFFFFF;
    }
    QPushButton#light_theme_button:pressed {
        background-color: #E5E7EB;
    }
    QPushButton#dark_theme_button {
        background-color: #111827;
        color: #F9FAFB;

        border: 1px solid #4B5563;
    }
    QPushButton#dark_theme_button:hover {
        background-color: #374151;
        border: 1px solid #60A5FA;
    }
    QPushButton#dark_theme_button:pressed {
        background-color: #0F172A;
    }

    /* ---------- Languages ---------- */
    QRadioButton#language_pt,
    QRadioButton#language_en,
    QRadioButton#language_es {
        color: #F9FAFB;

        font-size: 14px;
    }
    QRadioButton#language_pt::indicator,
    QRadioButton#language_en::indicator,
    QRadioButton#language_es::indicator {
        width: 18px;
        height: 18px;

        border-radius: 9px;

        border: 2px solid #6B7280;
        background: #111827;
    }
    QRadioButton#language_pt::indicator:hover,
    QRadioButton#language_en::indicator:hover,
    QRadioButton#language_es::indicator:hover {
        border: 2px solid #60A5FA;
    }
    QRadioButton#language_pt::indicator:checked,
    QRadioButton#language_en::indicator:checked,
    QRadioButton#language_es::indicator:checked {
        background: #3B82F6;
        border: 2px solid #3B82F6;
    }

    /* ---------- Notifications ---------- */
    #notifications_checkbox {
        color: #F9FAFB;

        font-size: 14px;
    }
    QCheckBox#notifications_checkbox::indicator {
        width: 18px;
        height: 18px;

        border-radius: 6px;

        border: 2px solid #6B7280;
        background: #111827;
    }
    QCheckBox#notifications_checkbox::indicator:hover {
        border: 2px solid #60A5FA;
    }
    QCheckBox#notifications_checkbox::indicator:checked {
        background: #3B82F6;
        border: 2px solid #3B82F6;
    }
"""