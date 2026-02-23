import os
from interfaces.data_source import ILogSource
from typing import List

class FileLogSource(ILogSource):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_logs(self) -> List[str]:
        if not os.path.exists(self.file_path):
            return [f"Error: File {self.file_path} not found."]
        
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file.readlines()]