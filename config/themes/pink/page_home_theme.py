PAGE_HOME = """
    #header_text {
        border: none;
        color: #1F2937;
        font-size: 26px;
        font-weight: 600;
    }

    #header_button {
        background-color: #FFFFFF;
        color: #1F2937;
        border: 1px solid #F3D6E0;
        border-radius: 10px;
        padding: 8px 14px;
        font-size: 14px;
        font-weight: 600;
    }

    #header_button:hover {
        background-color: #FFF0F6;
        border: 1px solid #EC4899;
    }

    #header_button:pressed {
        background-color: #FCE7F3;
        border: 1px solid #DB2777;
    }


    #today_tasks_text {
        border: none;
        color: #1F2937;
        font-size: 18px;
        font-weight: 600;
    }

    #upcoming_tasks_text {
        border: none;
        color: #1F2937;
        font-size: 18px;
        font-weight: 600;
    }


    #page_home_side {
        border: none;
    }


    /* ---------- Calendar ---------- */

    QCalendarWidget#calendar {
        background-color: #FFFFFF;
        border: 1px solid #F3D6E0;
        border-radius: 12px;
    }

    /* Fundo interno */
    QCalendarWidget#calendar QWidget {
        background-color: #FFFFFF;
        color: #1F2937;
    }


    /* Barra de navegação */
    QCalendarWidget#calendar QToolButton {
        background: transparent;
        color: #831843;
        border: none;
        font-size: 14px;
        font-weight: 600;
        padding: 6px;
        border-radius: 8px;
    }

    QCalendarWidget#calendar QToolButton:hover {
        background-color: #FCE7F3;
    }


    QCalendarWidget#calendar QToolButton::menu-indicator {
        image: none;
    }


    /* Cabeçalho (Dom Seg Ter...) */
    QCalendarWidget#calendar QHeaderView::section {
        background: transparent;
        color: #9D174D;
        border: none;
        font-weight: bold;
        padding: 6px;
    }


    /* Dias */
    QCalendarWidget#calendar QAbstractItemView {
        background-color: #FFFFFF;
        color: #1F2937;
        border: none;
        outline: 0;
        selection-background-color: #EC4899;
        selection-color: white;
        alternate-background-color: #FFFFFF;
    }


    /* Hover */
    QCalendarWidget#calendar QAbstractItemView:item:hover {
        background-color: #FCE7F3;
        border-radius: 8px;
    }


    /* Cards */
    #frame_home_calendar {
        background-color: #FFFFFF;
        border: 1px solid #F3D6E0;
        border-radius: 14px;
    }

    #frame_home_statistics {
        background-color: #FFFFFF;
        border: 1px solid #F3D6E0;
        border-radius: 14px;
    }


    #page_home_statistics_text {
        border: none;
        color: #1F2937;
        font-size: 18px;
        font-weight: 600;
    }


    #page_home_statistics_all,
    #page_home_statistics_completed,
    #page_home_statistics_pending {
        background-color: #FFF7FA;
        border: 1px solid #F3D6E0;
        border-radius: 12px;
        color: #1F2937;
        padding: 10px;
        font-size: 14px;
        font-weight: 500;
    }


    #page_home_statistics_all:hover,
    #page_home_statistics_completed:hover,
    #page_home_statistics_pending:hover {
        border: 1px solid #EC4899;
        background-color: #FFF0F6;
    }


    #frame_home {
        border: 1px solid #F3D6E0;
        border-radius: 10px;
    }


    /* Checkbox */
    QCheckBox#page_home_button::indicator {
        width: 18px;
        height: 18px;
        background-color: #FFFFFF;
        border: 2px solid #F3D6E0;
        border-radius: 6px;
    }


    QCheckBox#page_home_button::indicator:hover {
        border: 2px solid #EC4899;
        background-color: #FFF0F6;
    }


    QCheckBox#page_home_button::indicator:checked {
        background-color: #EC4899;
        border: 2px solid #EC4899;
    }


    #page_home_text {
        border: none;
        color: #1F2937;
        font-size: 15px;
        font-weight: 500;
    }


    #page_home_text2 {
        border: none;
        color: #9CA3AF;
        font-size: 13px;
        font-weight: 500;
    }
"""