from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from pathlib import Path
import os

# self.btn_1 = PyPushButton(text = "Ocultar menu")

class homeButton(QPushButton):
    def __init__(
            self,
            text = "",
            height = 40,
            minimum_width = 500,
            text_padding = 55,
            text_color = "#c3ccdf",
            icon_path = "",
            icon_color = "#c3ccdf",
            btn_color = "#44475a",
            btn_hover = "#4f5368",
            btn_pressed = "#282a36",
            is_activate = False
    ):
        super().__init__()

        # Set default parameters
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        # Custom parameters
        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_activate = is_activate

        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_activate = self.is_activate
        )

    def set_style(
        self,
        text_padding = 55,
        text_color = "#c3ccdf",
        btn_color = "#44475a",
        btn_hover = "#4f5368",
        btn_pressed = "#282a36",
        is_activate = False   
    ):
        style = f"""
        QPushButton{{
            color: {text_color};
            background-color: {btn_color};
            padding-left : {text_padding}px;
            text-align : left;
            border: none;
        }}
        QPushButton:hover {{
            background-color: {btn_hover};
        }}
        QPushButton:pressed {{
            background-color : {btn_pressed};
        }}
        """

        if is_activate:
            style += """
        QPushButton {
            background-color: red;
            border-right: 5px solid yellow;
        }
        """

        self.setStyleSheet(style)

    def set_active(self, active):
        self.is_activate = active

        self.set_style(
            text_padding=self.text_padding,
            text_color=self.text_color,
            btn_color=self.btn_color,
            btn_hover=self.btn_hover,
            btn_pressed=self.btn_pressed,
            is_activate=self.is_activate
        )