# Good example of following Single Responsibility Principle (SRP)
class ReportGenerator:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        report = f"Report generated with data: {self.data}"
        return report

class ReportSaver:
    def __init__(self, report):
        self.report = report

    def save_report(self, filename):
        with open(filename, 'w') as file:
            file.write(self.report)

class ReportManager:
    def __init__(self, data):
        self.report_generator = ReportGenerator(data)
        self.report_saver = None

    def create_and_save_report(self, filename):
        report = self.report_generator.generate_report()
        self.report_saver = ReportSaver(report)
        self.report_saver.save_report(filename)