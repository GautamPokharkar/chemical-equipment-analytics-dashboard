import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QVBoxLayout, QHBoxLayout, QFileDialog, QFrame
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

API_URL = "http://127.0.0.1:8000/api/upload/"


class PieChart(FigureCanvas):
    def __init__(self):
        self.fig = Figure(figsize=(4.5, 4.5))
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)

    def plot(self, data):
        self.ax.clear()
        labels = list(data.keys())
        values = list(data.values())
        colors = ['#ff6384', '#36a2eb', '#ffce56', '#4bc0c0', '#9966ff', '#ff9f40']

        self.ax.pie(
            values,
            labels=labels,
            startangle=90,
            colors=colors
        )
        self.ax.set_title("Equipment Type Distribution")
        self.draw()

class SummaryBox(QFrame):
    def __init__(self, title):
        super().__init__()
        self.setFrameShape(QFrame.StyledPanel)
        self.setStyleSheet(
            "QFrame { border: 1px solid #ddd; border-radius: 6px; padding: 10px; }"
        )

        layout = QVBoxLayout()
        self.title_label = QLabel(title)
        self.title_label.setStyleSheet("font-weight: bold;")

        self.value_label = QLabel("-")
        self.value_label.setStyleSheet("font-size: 14px;")

        layout.addWidget(self.title_label)
        layout.addWidget(self.value_label)
        self.setLayout(layout)

    def set_value(self, value):
        self.value_label.setText(value)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chemical Equipment Parameter Visualizer")
        self.resize(1100, 700)
        self.init_ui()
        self.setStyleSheet("""
        QWidget {
            background-color: qlineargradient(
                x1:0, y1:0, x2:0, y2:1,
                stop:0 #6f7bf7,
                stop:1 #7b5dc7
            );
            color:'white';
        }
        """)
    def download_pdf(self):
        try:
            import webbrowser
            webbrowser.open("http://127.0.0.1:8000/api/report/")
        except Exception as e:
            print("PDF download failed:", e)

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(20)

        title = QLabel("Chemical Equipment Parameter Visualizer")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 22px; font-weight: bold;")

        subtitle = QLabel("Upload and analyze your equipment data")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("color: #666;")

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        self.upload_btn = QPushButton("Upload CSV")
        self.upload_btn.setFixedHeight(35)
        self.upload_btn.clicked.connect(self.upload_csv)
        main_layout.addWidget(self.upload_btn, alignment=Qt.AlignLeft)
        self.pdf_btn = QPushButton("Download PDF Report")
        self.pdf_btn.setFixedHeight(35)
        self.pdf_btn.clicked.connect(self.download_pdf)

        main_layout.addWidget(self.pdf_btn, alignment=Qt.AlignLeft)

        content_layout = QHBoxLayout()
        content_layout.setSpacing(25)

        summary_layout = QVBoxLayout()
        summary_title = QLabel("Summary")
        summary_title.setStyleSheet("font-size: 16px; font-weight: bold;")
        summary_layout.addWidget(summary_title)

        self.total_box = SummaryBox("Total Equipment")
        self.flow_box = SummaryBox("Average Flowrate")
        self.pressure_box = SummaryBox("Average Pressure")
        self.temp_box = SummaryBox("Average Temperature")

        summary_layout.addWidget(self.total_box)
        summary_layout.addWidget(self.flow_box)
        summary_layout.addWidget(self.pressure_box)
        summary_layout.addWidget(self.temp_box)
        summary_layout.addStretch()

        summary_container = QWidget()
        summary_container.setLayout(summary_layout)
        summary_container.setFixedWidth(350)

        self.chart = PieChart()

        content_layout.addWidget(summary_container)
        content_layout.addWidget(self.chart)

        main_layout.addLayout(content_layout)
        self.setLayout(main_layout)

    def upload_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select CSV", "", "CSV Files (*.csv)"
        )
        if not file_path:
            return
        with open(file_path, "rb") as f:
            response = requests.post(API_URL, files={"file": f})
        data = response.json()

        self.total_box.set_value(str(data["total"]))
        self.flow_box.set_value(f"{data['avg_flowrate']:.2f}")
        self.pressure_box.set_value(f"{data['avg_pressure']:.2f}")
        self.temp_box.set_value(f"{data['avg_temperature']:.2f}")

        self.chart.plot(data["type_distribution"])

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
