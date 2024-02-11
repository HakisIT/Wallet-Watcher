from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox, QPushButton, QLCDNumber
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
import datetime
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.layout = QVBoxLayout()
        self.wid = QWidget()
        self.balance = QLineEdit()

        button_new_transaction = QPushButton()
        button_edit_transaction = QPushButton()
        button_delete_transaction = QPushButton()

        button_new_transaction.setText("new")
        button_edit_transaction.setText("edit")
        button_delete_transaction.setText("delede")
        
        # # # # # #
        hbox = QHBoxLayout()
        flo = QFormLayout()
        date_now = datetime.datetime.now()

        self.e1 = QLineEdit()
        self.e1.setValidator(QIntValidator())
        self.e1.setAlignment(Qt.AlignRight)

        e2 = QDateEdit()
        e2.setAlignment(Qt.AlignRight)
        d = QDate(int(str(date_now).split('-')[0]), int(str(date_now).split('-')[1]), int(str(date_now).split('-')[2][:2]))
        e2.setDate(d)
        
        e3 = QLineEdit()
        e3.setAlignment(Qt.AlignRight)

        self.r1 = QRadioButton("Expenditure")
        self.r2 = QRadioButton("Income")

        hbox.addWidget(self.r1)
        hbox.addWidget(self.r2)

        self.b1 = QPushButton("Submit")

        flo.addRow(QLabel("Type"),hbox)
        flo.addRow("date validator", e2)
        flo.addRow("integer validator", self.e1)
        flo.addRow("category", e3)
        flo.addRow(self.b1)

        self.b1.clicked.connect(self.func_balance_change)
        self.wid.setLayout(flo)
        self.wid.hide()
        # # # # # #

        button_new_transaction.clicked.connect(self.func_show)

        self.layout.addWidget(self.wid)
        self.layout.addWidget(button_new_transaction)
        self.layout.addWidget(button_edit_transaction)
        self.layout.addWidget(button_delete_transaction)
        self.layout.addWidget(self.balance)
        
        self.setLayout(self.layout)
        


    # def func_new_transaction(self):
    #     hbox = QHBoxLayout()
    #     flo = QFormLayout()
    #     date_now = datetime.datetime.now()

    #     self.e1 = QLineEdit()
    #     self.e1.setValidator(QIntValidator())
    #     self.e1.setAlignment(Qt.AlignRight)

    #     e2 = QDateEdit()
    #     e2.setAlignment(Qt.AlignRight)
    #     d = QDate(int(str(date_now).split('-')[0]), int(str(date_now).split('-')[1]), int(str(date_now).split('-')[2][:2]))
    #     e2.setDate(d)
        
    #     e3 = QLineEdit()
    #     e3.setAlignment(Qt.AlignRight)

    #     self.r1 = QRadioButton("Expenditure")
    #     self.r2 = QRadioButton("Income")

    #     hbox.addWidget(self.r1)
    #     hbox.addWidget(self.r2)

    #     self.b1 = QPushButton("Submit")

    #     flo.addRow(QLabel("Type"),hbox)
    #     flo.addRow("date validator", e2)
    #     flo.addRow("integer validator", self.e1)
    #     flo.addRow("category", e3)
    #     flo.addRow(self.b1)

    #     self.b1.clicked.connect(self.func_balance_change)
    #     self.wid.setLayout(flo)
    #     self.wid.show()

    def func_balance_change(self):
        if self.r1.isChecked():
            self.balance.setText(str(-abs(int(self.e1.text()))))
        else:
            self.balance.setText(self.e1.text())

        self.balance.setReadOnly(True)
        self.wid.hide()
        

    def func_show(self):
        self.wid.show()

    # def func_hide(self):
        
        














if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())