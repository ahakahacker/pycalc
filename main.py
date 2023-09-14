from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
import sys
from ui import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

def one():
    text = ui.lineEdit.text() + '1'
    ui.lineEdit.setText(text)

def two():
    text = ui.lineEdit.text() + '2'
    ui.lineEdit.setText(text)

def three():
    text = ui.lineEdit.text() + '3'
    ui.lineEdit.setText(text)

def four():
    text = ui.lineEdit.text() + '4'
    ui.lineEdit.setText(text)

def five():
    text = ui.lineEdit.text() + '5'
    ui.lineEdit.setText(text)

def six():
    text = ui.lineEdit.text() + '6'
    ui.lineEdit.setText(text)

def seven():
    text = ui.lineEdit.text() + '7'
    ui.lineEdit.setText(text)

def eight():
    text = ui.lineEdit.text() + '8'
    ui.lineEdit.setText(text)

def nine():
    text = ui.lineEdit.text() + '9'
    ui.lineEdit.setText(text)

def zero():
    text = ui.lineEdit.text() + '0'
    ui.lineEdit.setText(text)

def dot():
    text = ui.lineEdit.text() + '.'
    ui.lineEdit.setText(text)

def plus():
    text = ui.lineEdit.text() + '+'
    ui.lineEdit.setText(text)

def minus():
    text = ui.lineEdit.text() + '-'
    ui.lineEdit.setText(text)

def mult():
    text = ui.lineEdit.text() + '*'
    ui.lineEdit.setText(text)

def division():
    text = ui.lineEdit.text() + '/'
    ui.lineEdit.setText(text)

def equals():
    expression = ui.lineEdit.text()
    if any(char.isalpha() for char in expression):
        ui.lineEdit.setText('')
        QMessageBox.critical(None, "Ошибка", "Пример не должен содержать букв.")
    else:
        try:
            try:
                result = eval(expression)
                ui.lineEdit.setText(str(result))
            except SyntaxError:
                QMessageBox.critical(None, "Ошибка", "Ошибка, поле ввода пусто?")
        except ZeroDivisionError:
            ui.lineEdit.setText('')
            QMessageBox.critical(None, "Ошибка", "На ноль делить нельзя!")

def close():
    sys.exit()

def minimize():
    MainWindow.showMinimized()

ui.pushButton.clicked.connect(one)
ui.pushButton_2.clicked.connect(two)
ui.pushButton_3.clicked.connect(three)
ui.pushButton_4.clicked.connect(four)
ui.pushButton_5.clicked.connect(five)
ui.pushButton_6.clicked.connect(six)
ui.pushButton_7.clicked.connect(seven)
ui.pushButton_8.clicked.connect(eight)
ui.pushButton_9.clicked.connect(nine)
ui.pushButton_10.clicked.connect(zero)
ui.pushButton_11.clicked.connect(dot)
ui.pushButton_14.clicked.connect(plus)
ui.pushButton_15.clicked.connect(minus)
ui.pushButton_16.clicked.connect(mult)
ui.pushButton_17.clicked.connect(division)
ui.pushButton_13.clicked.connect(equals)
ui.pushButton_12.clicked.connect(close)
ui.pushButton_18.clicked.connect(minimize)

sys.exit(app.exec_())