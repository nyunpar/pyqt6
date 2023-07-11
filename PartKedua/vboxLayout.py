from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 QHBox Layout Example")
        self.setWindowIcon(QIcon("images/python.png"))

        vbox = QVBoxLayout()

        btn1 = QPushButton("Klik Satu")
        btn2 = QPushButton("Klik Dua")
        btn3 = QPushButton("Klik Tiga")
        btn4 = QPushButton("Klik Empat")

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)
        # vbox.addSpacing(100)
        vbox.addStretch(5)

        self.setLayout(vbox)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
