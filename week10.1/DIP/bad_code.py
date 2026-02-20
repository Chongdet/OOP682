# DIP code example bad_code.py
# Bad example of violating Dependency Inversion Principle (DIP)
# High-level module (ReportGenerator) depends on low-level module (Database) directly
# ทำให้ยากต่อการเปลี่ยนแปลงหรือทดสอบ ReportGenerator
# ถ้าต้องการเปลี่ยนแหล่งข้อมูล ต้องแก้ไขโค้ดใน ReportGenerator ด้วย

class Database:
    def get_data(self):
        return "Data from Database"
class ReportGenerator:
    def __init__(self):
        self.database = Database()  # High-level module depends on low-level module directly

    def generate_report(self):
        data = self.database.get_data()
        report = f"Report generated with data: {data}"
        return report
# Example usage
report_generator = ReportGenerator()
print(report_generator.generate_report())  # Output: Report generated with data: Data from Database
# To follow DIP, we should depend on abstractions (e.g., interfaces) rather than concrete implementations.
# แปลว่า ReportGenerator ควรจะขึ้นอยู่กับ interface ของแหล่งข้อมูล ไม่ใช่กับ Database โดยตรง