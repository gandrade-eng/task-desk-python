PAGE_HOME = """
    #header_text {
        border: none;
        color: #111827;
        font-size: 26px;
        font-weight: 600;
    }
    #header_button {
        background-color: #FFFFFF;
        color: #111827;
        border: 1px solid #D1D5DB;
        border-radius: 10px;
        padding: 8px 14px;
        font-size: 14px;
        font-weight: 600;
    }
    #header_button:hover {
        background-color: #F3F4F6;
        border: 1px solid #3B82F6;
    }
    #header_button:pressed {
        background-color: #E5E7EB;
        border: 1px solid #2563EB;
    }
    #today_tasks_text {
        border: none;
        color: #111827;

        font-size: 18px;
        font-weight: 600;
    }
    #upcoming_tasks_text {
        border: none;
        color: #111827;
        font-size: 18px;
        font-weight: 600;
    }
    #page_home_side {
        border: none
    }

    /* ---------- Calendar ---------- */
    QCalendarWidget#calendar {
        background-color: #FFFFFF;
        border: 1px solid #D9DCE3;
        border-radius: 12px;
    }

    /* Fundo interno */
    QCalendarWidget#calendar QWidget {
        background-color: #FFFFFF;
        color: #222222;
    }

    /* Barra de navegação */
    QCalendarWidget#calendar QToolButton {
        background: transparent;
        color: #2C3E50;
        border: none;
        font-size: 14px;
        font-weight: 600;
        padding: 6px;
        border-radius: 8px;
    }

    QCalendarWidget#calendar QToolButton:hover {
        background-color: #EEF2F7;
    }

    /* Remove a setinha do menu */
    QCalendarWidget#calendar QToolButton::menu-indicator {
        image: none;
    }

    /* Cabeçalho (Dom Seg Ter...) */
    QCalendarWidget#calendar QHeaderView::section {
        background: transparent;
        color: #6B7280;
        border: none;
        font-weight: bold;
        padding: 6px;
    }

    /* Dias */
    QCalendarWidget#calendar QAbstractItemView {
        background-color: #FFFFFF;
        color: #222222;
        border: none;
        outline: 0;
        selection-background-color: #4F8EF7;
        selection-color: white;
        alternate-background-color: #FFFFFF;
    }

    /* Hover */
    QCalendarWidget#calendar QAbstractItemView:item:hover {
        background-color: #E8F1FF;
        border-radius: 8px;
    }

    /* frame calendar */
    #frame_home_calendar {
        background-color: #FFFFFF;

        border: 1px solid #E5E7EB;
        border-radius: 14px;
    }
    #frame_home_statistics {
        background-color: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-radius: 14px;
    }
    #page_home_statistics_text {
        border: none;
        color: #111827;
        font-size: 18px;
        font-weight: 600;
    }
    #page_home_statistics_all,
    #page_home_statistics_completed,
    #page_home_statistics_pending {
        background-color: #F9FAFB;
        border: 1px solid #E5E7EB;
        border-radius: 12px;
        color: #111827;
        padding: 10px;
        font-size: 14px;
        font-weight: 500;
    }
    #page_home_statistics_all:hover,
    #page_home_statistics_completed:hover,
    #page_home_statistics_pending:hover {
        border: 1px solid #3B82F6;
        background-color: #F3F4F6;
    }
    #frame_home {
        border: 1px solid black;
        border-radius: 10px;
    }
    QCheckBox#page_home_button::indicator {
        width: 18px;
        height: 18px;
        background-color: #FFFFFF;
        border: 2px solid #D1D5DB;
        border-radius: 6px;
    }
    QCheckBox#page_home_button::indicator:hover {
        border: 2px solid #3B82F6;
        background-color: #EFF6FF;
    }
    QCheckBox#page_home_button::indicator:checked {
        background-color: #3B82F6;
        border: 2px solid #3B82F6;
    }
    #page_home_text {
        border: none;
        color: #111827;
        font-size: 15px;
        font-weight: 500;
    }
    #page_home_text2 {
        border: none;
        color: #6B7280;
        font-size: 13px;
        font-weight: 500;
    }
"""