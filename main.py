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
        self.balance.setText('0')

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

        self.current_date = QDateEdit()
        self.current_date.setAlignment(Qt.AlignRight)
        d = QDate(int(str(date_now).split('-')[0]), int(str(date_now).split('-')[1]), int(str(date_now).split('-')[2][:2]))
        self.current_date.setDate(d)
        
        self.e3 = QLineEdit()
        self.e3.setAlignment(Qt.AlignRight)

        self.r1 = QRadioButton("Expenditure")
        self.r2 = QRadioButton("Income")

        hbox.addWidget(self.r1)
        hbox.addWidget(self.r2)

        self.b1 = QPushButton("Submit")

        flo.addRow(QLabel("Type"),hbox)
        flo.addRow("date validator", self.current_date)
        flo.addRow("integer validator", self.e1)
        flo.addRow("category", self.e3)
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


    def func_balance_change(self):
        if self.r1.isChecked():
            negative_number_calculation = str(int(self.e1.text()) - int(self.balance.text()))
            self.balance.setText(str(-int(negative_number_calculation)))
        else:
            self.positive_number_calculation = str(int(self.e1.text()) + int(self.balance.text()))
            self.balance.setText(self.positive_number_calculation)
            self.func_add_transaction_file()
            

        self.e1.clear()
        self.e3.clear()
        self.balance.setReadOnly(True)
        self.wid.hide()


    def func_add_transaction_file(self):
        with open('D:/Project/Wallet-Watcher/balance_sheet_actions.txt', 'a', encoding="utf8") as file:
            file.write(f'Income: {self.positive_number_calculation}, Category: {self.e3.text()}, Date: {self.current_date.text()}')


    def func_show(self):
        self.wid.show()
        
        














if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())