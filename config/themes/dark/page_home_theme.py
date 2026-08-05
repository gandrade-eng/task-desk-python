PAGE_HOME = """
    #header_text {
        border: none;
        color: #F9FAFB;
        font-size: 26px;
        font-weight: 600;
    }

    #header_button {
        background-color: #1F2937;
        color: #F9FAFB;

        border: 1px solid #4B5563;
        border-radius: 10px;

        padding: 8px 14px;

        font-size: 14px;
        font-weight: 600;
    }

    #header_button:hover {
        background-color: #374151;
        border: 1px solid #60A5FA;
    }

    #header_button:pressed {
        background-color: #111827;
        border: 1px solid #3B82F6;
    }

    #today_tasks_text {
        border: none;

        color: #F9FAFB;

        font-size: 18px;
        font-weight: 600;
    }

    #upcoming_tasks_text {
        border: none;

        color: #F9FAFB;

        font-size: 18px;
        font-weight: 600;
    }

    #page_home_side {
        border: none;
    }

    /* ---------- Calendar ---------- */
    QCalendarWidget#calendar {
        background-color: #252733;
        border: 1px solid #353849;
        border-radius: 12px;
    }

    /* Fundo interno */
    QCalendarWidget#calendar QWidget {
        background-color: #252733;
        color: #F2F2F2;
    }

    /* Barra de navegação */
    QCalendarWidget#calendar QToolButton {
        background: transparent;
        color: white;
        border: none;
        font-size: 14px;
        font-weight: 600;
        padding: 6px;
        border-radius: 8px;
    }

    QCalendarWidget#calendar QToolButton:hover {
        background-color: #3A3E52;
    }

    /* Remove a setinha do menu */
    QCalendarWidget#calendar QToolButton::menu-indicator {
        image: none;
    }

    /* Cabeçalho */
    QCalendarWidget#calendar QHeaderView::section {
        background: transparent;
        color: #A8AFBD;
        border: none;
        font-weight: bold;
        padding: 6px;
    }

    /* Dias */
    QCalendarWidget#calendar QAbstractItemView {
        background-color: #252733;
        color: white;
        border: none;
        outline: 0;
        selection-background-color: #6C63FF;
        selection-color: white;
        alternate-background-color: #252733;
    }

    /* Hover */
    QCalendarWidget#calendar QAbstractItemView:item:hover {
        background-color: #3C4057;
        border-radius: 8px;
    }

    /* FRAME CALENDAR */
    #frame_home_calendar {
        background-color: #1F2937;

        border: 1px solid #374151;
        border-radius: 14px;
    }

    #frame_home_statistics {
        background-color: #1F2937;

        border: 1px solid #374151;
        border-radius: 14px;
    }

    #page_home_statistics_text {
        border: none;

        color: #F9FAFB;

        font-size: 18px;
        font-weight: 600;
    }

    #page_home_statistics_all,
    #page_home_statistics_completed,
    #page_home_statistics_pending {
        background-color: #111827;

        border: 1px solid #374151;
        border-radius: 12px;

        color: #F9FAFB;

        padding: 10px;

        font-size: 14px;
        font-weight: 500;
    }

    #page_home_statistics_all:hover,
    #page_home_statistics_completed:hover,
    #page_home_statistics_pending:hover {
        background-color: #1F2937;
        border: 1px solid #60A5FA;
    }

    #frame_home {
        background-color: #1F2937;

        border: 1px solid #374151;
        border-radius: 10px;
    }

    QCheckBox#page_home_button::indicator {
        width: 18px;
        height: 18px;

        background-color: #111827;

        border: 2px solid #6B7280;
        border-radius: 6px;
    }

    QCheckBox#page_home_button::indicator:hover {
        border: 2px solid #60A5FA;
        background-color: #1E3A8A;
    }

    QCheckBox#page_home_button::indicator:checked {
        background-color: #3B82F6;
        border: 2px solid #3B82F6;
    }

    #page_home_text {
        border: none;

        color: #F9FAFB;

        font-size: 15px;
        font-weight: 500;
    }

    #page_home_text2 {
        border: none;

        color: #D1D5DB;

        font-size: 13px;
        font-weight: 500;
    }
"""