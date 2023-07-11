from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 Grid Layout Example")
        self.setWindowIcon(QIcon("images/python.png"))

        grid = QGridLayout()

        btn1 = QPushButton("Klik Satu")
        btn2 = QPushButton("Klik Dua")
        btn3 = QPushButton("Klik Tiga")
        btn4 = QPushButton("Klik Empat")
        btn5 = QPushButton("Klik Lima")
        btn6 = QPushButton("Klik Enam")
        btn7 = QPushButton("Klik Tujuh")
        btn8 = QPushButton("Klik Delapan")

        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 0, 1)
        grid.addWidget(btn3, 0, 2)
        grid.addWidget(btn4, 0, 3)
        grid.addWidget(btn5, 1, 0)
        grid.addWidget(btn6, 1, 1)
        grid.addWidget(btn7, 1, 2)
        grid.addWidget(btn8, 1, 3)
        # grid.addSpacing(100)
        # grid.addStretch(5)

        self.setLayout(grid)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
