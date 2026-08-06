ADD_TASK = """
    #form {
        color: #1F2937;
    }

    #title_input_label,
    #date_input_label,
    #time_input_label,
    #description_input_label {
        color: #374151;
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
        border: 1px solid #F3D6E0;
        border-radius: 8px;
        padding: 8px;
        selection-background-color: #EC4899;
        font-size: 14px;
    }

    #title_input:hover,
    #date_input:hover,
    #time_input:hover,
    #description_input:hover {
        border: 1px solid #F472B6;
    }

    #title_input:focus,
    #date_input:focus,
    #time_input:focus,
    #description_input:focus {
        border: 2px solid #EC4899;
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
        background-color: #EC4899;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 8px 16px;
    }

    #options_send:hover {
        background-color: #DB2777;
    }

    #options_send:pressed {
        background-color: #BE185D;
    }

    #options_cancel {
        background-color: #FFF0F6;
        color: #374151;
        border: 1px solid #F3D6E0;
        border-radius: 8px;
        padding: 8px 16px;
    }

    #options_cancel:hover {
        background-color: #FCE7F3;
    }

    #options_cancel:pressed {
        background-color: #FBCFE8;
    }
"""