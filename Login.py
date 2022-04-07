import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QMessageBox, QTableWidget,QTableWidgetItem, QHeaderView, QDesktopWidget
from PyQt5 import QtGui,QtCore
from PyQt5.QtCore import pyqtSlot
from FilesOperations.ListaUtenti import *

class Button(QWidget):
    def __init__(self, name, widget, x, y, event):

        self.button = QPushButton(widget)
        #self.button.initStyleOption('Blackadder ITC')
        self.button.setText(name)
        self.button.move(x, y)
        self.button.clicked.connect(event)

class Login(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        Pagina(self, "Login")

        self.line_edit = QLineEdit()

        self.label = QLabel(self)
        self.label.move(25, 20)
        self.label.setFont(QtGui.QFont('Castellar', int(H/15)))
        self.label.setText("Inserisci il tuo username")
        self.button1 = Button("Indietro", self, 10, 417, self.Indietro)
        self.Text = QLineEdit(self)
        self.Text.move(170, 220)
        print(self.frameGeometry().center())
        self.Button2 = Button('Entra', self,  305, 219, self.Entra)
        self.showMaximized()


    @pyqtSlot()
    def Entra(self):
        TextE = self.textbox.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + TextE, QMessageBox.Ok,
                             QMessageBox.Ok)
        self.textbox.setText("")


    @pyqtSlot()
    def Indietro(self):
        self.app = App()
        self.app.show()
        self.close()


class App(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        Pagina(self, "Hobby")

        self.Buttons()

    def Buttons(self):
        button = QPushButton("LOGIN", self)
        button.resize(int(W/4), int(H/9))
        button.move(int(W*3/8), int(H*2/5))
        self.showMaximized()

        #self.button.setFont(QtGui.QFont('Blackadder ITC', 10))

        # adding action to a button
        button.clicked.connect(self.Login)

        self.show()


    def Login(self):
        self.login = Login()
        self.login.show()
        self.close()

def Pagina(self, nome):
    self.setWindowTitle(nome)
    self.setGeometry(300, 300, W, H)
    self.setMinimumSize(W, H)

def main():
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    size = screen.size()
    global H
    global W
    H = size.height()
    W = size.width()
    Applicazione = App()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()