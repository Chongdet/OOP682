# Good example of following Dependency Inversion Principle (DIP)
from abc import ABC, abstractmethod
class DatabaseInterface(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass
class MySQLDatabase(DatabaseInterface):
    def connect(self):
        print("Connecting to MySQL Database")

    def disconnect(self):
        print("Disconnecting from MySQL Database")

class ReportGenerator:
    def __init__(self, database: DatabaseInterface):
        self.database = database  # High-level module depends on abstraction (interface)

    def generate_report(self):
        self.database.connect()
        data = "Data from Database"  # Simulate data retrieval
        report = f"Report generated with data: {data}"
        self.database.disconnect()
        return report

# Example usage
mysql_db = MySQLDatabase()
report_generator = ReportGenerator(mysql_db)
print(report_generator.generate_report())  # Output: Report generated with data: Data from Database
#หมายถึง ReportGenerator ขึ้นอยู่กับ interface ของแหล่งข้อมูล (DatabaseInterface) แทนที่จะขึ้นอยู่กับ MySQLDatabase โดยตรง