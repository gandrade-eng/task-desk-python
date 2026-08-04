# external imports
from PySide6.QtWidgets import QApplication
import sys
# internal imports
from ui.main_window import MainWindow

def main():
    # QApplication gerencia a aplicação
    app = QApplication(sys.argv)
    # Cria a Janela
    window = MainWindow()
    # Cria o loop, experando eventos
    sys.exit(app.exec())

if __name__ == "__main__":
    main()