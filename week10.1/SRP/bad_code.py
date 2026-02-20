# S = Single Responsibility Principle (SRP)
#Bad example of violating SRP
class ReportManager:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        report = f"Report generated with data: {self.data}"
        return report

    def save_report(self, filename):
        report = self.generate_report()
        with open(filename, 'w') as file:
            file.write(report)
    