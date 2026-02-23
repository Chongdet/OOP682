import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from services.mock_source import MockLogSource
from services.file_source import FileLogSource
from services.csv_source import CsvLogSource

def main():
    app = QApplication(sys.argv)

    source = CsvLogSource("test_data.csv")
   
    window = MainWindow(source)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()