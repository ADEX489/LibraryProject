import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QMessageBox, QTableWidget,QTableWidgetItem, QHeaderView
from PyQt5 import QtGui,QtCore
from PyQt5.QtCore import pyqtSlot
from FilesOperations.ListaLibri import *
from FilesOperations.LibriInPossesso import *
from FilesOperations.ListaUtenti import *
from PyQt5.QtGui import *


class Button(QWidget):
    def __init__(self, name, widget, x, y, event, w, h):

        self.button = QPushButton(widget)
        #self.button.initStyleOption('Blackadder ITC')
        self.button.setText(name)
        self.button.move(x, y)
        self.button.resize(int(W / w), int(H / h))
        self.button.setFont(QFont("Eras Demi ITC", (int(H / 60))))
        self.button.clicked.connect(event)


class Utenti(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        Pagina(self, "Libri da restituire")

        self.Label()

        self.Buttons()

        self.showMaximized()

    def Label(self):
        self.label = QLabel(self)
        self.label.move(int(W/20), int(H/30))
        self.label.setFont(QtGui.QFont(Font, int(H/10)))
        self.label.setText("Libri da restituire")

    def Buttons(self):
        self.Indietro = Button("Indietro", self, int(W*3/4), int(H/22), self.Indietro, 7, 6)

    @pyqtSlot()
    def Indietro(self):
        self.app = App()
        self.app.show()
        self.close()

class Libri(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        Pagina(self, "Libri da restituire")

        self.Label()

        self.Buttons()

        self.showMaximized()

    def Label(self):
        self.label = QLabel(self)
        self.label.move(int(W/20), int(H/30))
        self.label.setFont(QtGui.QFont(Font, int(H/10)))
        self.label.setText("Libri da restituire")

    def Buttons(self):
        self.Indietro = Button("Indietro", self, int(W*3/4), int(H/22), self.Indietro, 7, 6)

    @pyqtSlot()
    def Indietro(self):
        self.app = App()
        self.app.show()
        self.close()

class LibriP(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        Pagina(self, "Libri da restituire")

        self.Label()

        self.Buttons()

        self.showMaximized()

    def Label(self):
        self.label = QLabel(self)
        self.label.move(int(W/20), int(H/30))
        self.label.setFont(QtGui.QFont(Font, int(H/10)))
        self.label.setText("Libri da restituire")

    def Buttons(self):
        self.Indietro = Button("Indietro", self, int(W*3/4), int(H/22), self.Indietro, 7, 6)

    @pyqtSlot()
    def Indietro(self):
        self.app = App()
        self.app.show()
        self.close()

class Ettichetta(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        Pagina(self, "Libri da restituire")

        self.Label()

        self.Buttons()

        self.showMaximized()

    def Label(self):
        self.label = QLabel(self)
        self.label.move(int(W/20), int(H/30))
        self.label.setFont(QtGui.QFont(Font, int(H/10)))
        self.label.setText("Libri da restituire")

    def Buttons(self):
        self.Indietro = Button("Indietro", self, int(W*3/4), int(H/22), self.Indietro, 7, 6)

    @pyqtSlot()
    def Indietro(self):
        self.app = App()
        self.app.show()
        self.close()


class App(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        Pagina(self, "Admin")

        self.Label()

        self.Buttons()

        self.showMaximized()

    def Label(self):
        self.label = QLabel(self)
        self.label.move(int(W/8), int(H/13))
        self.label.setFont(QtGui.QFont(Font, int(H/9)))
        self.label.setText("Interfaccia gestione")

    def Buttons(self):
        self.Button1 = Button("Lista Utenti", self, int(W/3) - int(W/15), int(H/2) - int(H/6), self.show_Utenti, 8, 5)
        self.Button2 = Button("Lista Libri", self, int(W*3/4) - int(W/8), int(H/2) - int(H/6), self.show_Libri, 8, 5)
        self.Button3 = Button("Libri in possesso", self, int(W/3) - int(W/15), int(H*3/4) - int(H/7), self.show_libriP, 8 ,5)
        self.Button4 = Button("Gestione Etichette", self, int(W*3/4) - int(W/8), int(H*3/4) - int(H/7), self.show_Etichette, 8, 5)

    def show_Utenti(self):
        self.libri = Utenti()
        self.libri.show()
        self.close()

    def show_Libri(self):
        self.libriR = Libri()
        self.libriR.show()
        self.close()

    def show_libriP(self):
        self.libriP = LibriP()
        self.libriP.show()
        self.close()

    def show_Etichette(self):
        self.Prestito = Ettichetta()
        self.Prestito.show()
        self.close()

def Pagina(self, nome):
    self.setWindowTitle(nome)
    self.setGeometry(300, 300, W, H)
    self.setMinimumSize(W, H)

def AdminLog():
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    size = screen.size()
    global H
    global W
    H = size.height()
    W = size.width()
    global Libreria
    Libreria = Biblioteca()
    global CurrentUser
    CurrentUser = "adex489"
    global Font
    Font = "Arial"
    Applicazione = App()
    sys.exit(app.exec_())


if __name__ == "__main__":
    AdminLog()