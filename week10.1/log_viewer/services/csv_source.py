import csv
import os
from interfaces.data_source import ILogSource 
from typing import List

class CsvLogSource(ILogSource): 
    def __init__(self, filename):
        self.filename = filename

    def get_logs(self) -> List[str]:
        if not os.path.exists(self.filename):
            return ["Error: หาไฟล์ CSV ไม่เจอครับ!"]

        result = []
        with open(self.filename, mode='r', encoding='utf-8') as f:
            data = csv.reader(f)
            for row in data:
                line = " | ".join(row)
                result.append(line)
        
        return result