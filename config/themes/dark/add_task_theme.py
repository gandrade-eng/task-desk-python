ADD_TASK = """
    #form {
        color: #F3F4F6;
    }

    #title_input_label,
    #date_input_label,
    #time_input_label,
    #description_input_label {
        color: #E9ECEF;
        font-size: 14px;
        font-weight: 600;
        padding-bottom: 4px;
    }

    #title_input,
    #date_input,
    #time_input,
    #description_input {
        background-color: #2D3748;
        color: #F3F4F6;
        border: 1px solid #4B5563;
        border-radius: 8px;
        padding: 8px;
        selection-background-color: #60A5FA;
        font-size: 14px;
    }

    #title_input:hover,
    #date_input:hover,
    #time_input:hover,
    #description_input:hover {
        border: 1px solid #6B7280;
    }

    #title_input:focus,
    #date_input:focus,
    #time_input:focus,
    #description_input:focus {
        border: 2px solid #60A5FA;
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

    #date_input::down-arrow,
    #time_input::down-arrow {
        image: url(icons/chevron_down_white.svg);
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
        background-color: #374151;
        color: white;
        border: 1px solid #4B5563;
        border-radius: 8px;
        padding: 8px 16px;
    }

    #options_cancel:hover {
        background-color: #4B5563;
    }

    #options_cancel:pressed {
        background-color: #6B7280;
    }
"""