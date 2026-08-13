# external imports
from PySide6.QtCore import Signal, QDate, QSize
from PySide6.QtGui import Qt, QTextCharFormat, QColor, QIcon
from PySide6.QtWidgets import (
    QFrame, QHBoxLayout, QVBoxLayout, 
    QLabel, QWidget, QPushButton, QCheckBox,
    QCalendarWidget, QGraphicsDropShadowEffect,
    QToolButton
)

# internal imports
from config import THEMES, LANGUAGES

class EditTask(QWidget):
    ...