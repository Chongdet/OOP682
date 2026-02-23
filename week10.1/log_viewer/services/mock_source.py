from interfaces.data_source import ILogSource
from typing import List

class MockLogSource(ILogSource): 
    def get_logs(self) -> List[str]:
        return [
            "2026-02-23 15:00:01 - INFO - System started",
            "2026-02-23 15:05:22 - WARNING - High memory usage",
            "2026-02-23 15:10:15 - ERROR - Database connection failed"
        ]