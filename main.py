from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox, QPushButton
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
import datetime
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.layout = QHBoxLayout()
        self.wid = QWidget()
        self.balance = QLabel('0', self) 

        button_new_transaction = QPushButton()
        button_edit_transaction = QPushButton()
        button_delete_transaction = QPushButton()

        button_new_transaction.setText("new")
        button_edit_transaction.setText("edit")
        button_delete_transaction.setText("delede")

        button_new_transaction.clicked.connect(self.func_new_transaction)

        self.layout.addWidget(button_new_transaction)
        self.layout.addWidget(button_edit_transaction)
        self.layout.addWidget(button_delete_transaction)
        self.layout.addWidget(self.balance)
        self.setLayout(self.layout)


    def func_new_transaction(self):
        hbox = QHBoxLayout()
        flo = QFormLayout()
        date_now = datetime.datetime.now()

        e1 = QLineEdit()
        e1.setValidator(QIntValidator())
        e1.setAlignment(Qt.AlignRight)

        e2 = QDateEdit()
        e2.setAlignment(Qt.AlignRight)
        d = QDate(int(str(date_now).split('-')[0]), int(str(date_now).split('-')[1]), int(str(date_now).split('-')[2][:2]))
        e2.setDate(d)
        
        e3 = QLineEdit()
        e3.setAlignment(Qt.AlignRight)

        r1 = QRadioButton("Expenditure")
        r2 = QRadioButton("Income")

        hbox.addWidget(r1)
        hbox.addWidget(r2)

        b1 = QPushButton("Submit")
        b2 = QPushButton("Cancel")

        flo.addRow(QLabel("Type"),hbox)
        flo.addRow("date validator", e2)
        flo.addRow("integer validator", e1)
        flo.addRow("category", e3)
        flo.addRow(b1)

        b1.clicked.connect(func_balance_change)

        self.wid.setLayout(flo)
        self.wid.show()

        def func_balance_change(self):
            # if r1.isChecked():
            #      - e1.text()
            # else:
            #     bal + e1.text()














if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())