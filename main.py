from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox, QPushButton
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.layout = QVBoxLayout()
        button_new_transaction = QPushButton()
        button_new_transaction.setText("Hello World!")
        button_new_transaction.clicked.connect(self.func_new_transaction)
        button_new_transaction.move(150, 300)
        self.layout.addWidget(button_new_transaction)
        self.setLayout(self.layout)

    def func_new_transaction():
        print('hello')













if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())