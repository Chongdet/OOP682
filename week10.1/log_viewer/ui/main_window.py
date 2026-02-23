from PySide6.QtWidgets import (QMainWindow, QVBoxLayout, QPushButton, 
                             QListWidget, QWidget, QLabel, QHBoxLayout)
from PySide6.QtGui import QFont
from interfaces.data_source import ILogSource

class MainWindow(QMainWindow):
    def __init__(self, source: ILogSource):
        super().__init__()
        self.source = source  
        self.init_ui()
        self.apply_styles()

    def init_ui(self):
        self.setWindowTitle("Professional Log Viewer")
        self.resize(900, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)


        header = QLabel("Real-time System Logs")
        header.setFont(QFont("Arial", 16, QFont.Bold))
        layout.addWidget(header)


        tool_layout = QHBoxLayout()
        self.btn_refresh = QPushButton("Refresh Logs")
        self.btn_refresh.clicked.connect(self.load_data)
        
        self.btn_filter = QPushButton("Show Errors Only")

        self.btn_filter.clicked.connect(lambda: self.load_data(filter_error=True))
        
        tool_layout.addWidget(self.btn_refresh)
        tool_layout.addWidget(self.btn_filter)
        tool_layout.addStretch()
        layout.addLayout(tool_layout)

        # List Display
        self.list_widget = QListWidget()
        self.list_widget.setFont(QFont("Consolas", 10))
        layout.addWidget(self.list_widget)

    def apply_styles(self):
        self.setStyleSheet("""
            QMainWindow { background-color: #2b2b2b; }
            QLabel { color: #e8e8e8; margin-bottom: 10px; }
            QPushButton { 
                background-color: #3c3f41; color: white; border: 1px solid #555;
                padding: 8px 15px; border-radius: 4px; 
            }
            QPushButton:hover { background-color: #4b4d4d; }
            QListWidget { 
                background-color: #1e1e1e; color: #a9b7c6; 
                border-radius: 5px; padding: 5px;
            }
        """)

    def load_data(self, filter_error=False):
        logs = self.source.get_logs()
        
        if filter_error:
            logs = [line for line in logs if "ERROR" in line.upper()] 
            
        self.list_widget.clear()
        self.list_widget.addItems(logs)