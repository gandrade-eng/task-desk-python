ADD_TASK = """
    #form {
        color: #1F2937;
    }

    #title_input_label,
    #date_input_label,
    #time_input_label,
    #description_input_label {
        color: #343A40;
        font-size: 14px;
        font-weight: 600;
        padding-bottom: 4px;
    }

    #title_input,
    #date_input,
    #time_input,
    #description_input {
        background-color: #FFFFFF;
        color: #1F2937;
        border: 1px solid #D1D5DB;
        border-radius: 8px;
        padding: 8px;
        selection-background-color: #3B82F6;
        font-size: 14px;
    }

    #title_input:hover,
    #date_input:hover,
    #time_input:hover,
    #description_input:hover {
        border: 1px solid #9CA3AF;
    }

    #title_input:focus,
    #date_input:focus,
    #time_input:focus,
    #description_input:focus {
        border: 2px solid #3B82F6;
    }

    /* TIME INPUT */
    QTimeEdit#time_input::up-button,
    QTimeEdit#time_input::down-button {
        width: 0px;
        height: 0px;
    }

    /* Botão do calendário e do horário */
    #date_input::drop-down,
    #time_input::drop-down {
        border: none;
        width: 24px;
    }

    #date_input::down-arrow {
        image: url(icons/chevron_down_black.svg);
    }

    #options_send {
        background-color: #3B82F6;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 8px 16px;
    }

    #options_send:hover {
        background-color: #2563EB;
    }

    #options_send:pressed {
        background-color: #1D4ED8;
    }

    #options_cancel {
        background-color: #F3F4F6;
        color: #374151;
        border: 1px solid #D1D5DB;
        border-radius: 8px;
        padding: 8px 16px;
    }

    #options_cancel:hover {
        background-color: #E5E7EB;
    }

    #options_cancel:pressed {
        background-color: #D1D5DB;
    }
"""