import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.clicked.connect(self.button_clicked)  # Connect button click to the function

        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(button)

    def button_clicked(self):
        print("Button was clicked!")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
