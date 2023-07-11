from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 Event Handling Example")
        self.setWindowIcon(QIcon("images/python.png"))

        self.create_widget()

    def create_widget(self):
        hbox = QHBoxLayout()
        btn = QPushButton("Ganti Teks")
        btn.clicked.connect(self.clicked_btn)
        self.label = QLabel("Teks Default")

        hbox.addWidget(btn)
        hbox.addWidget(self.label)
        self.setLayout(hbox)

    def clicked_btn(self):
        self.label.setText("Teks Lainnya")
        self.label.setFont(QFont("Times", 15))
        self.label.setStyleSheet('color:red')


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
