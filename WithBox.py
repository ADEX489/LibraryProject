import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QMessageBox, QTableWidget,QTableWidgetItem, QHeaderView
from PyQt5 import QtGui,QtCore
from PyQt5.QtCore import pyqtSlot
from FilesOperations.ListaLibri import *
from FilesOperations.LibriInPossesso import *
from FilesOperations.ListaUtenti import *
from PyQt5.QtGui import *

import pandas as pd
from pandas import ExcelWriter
import openpyxl

class Button(QWidget):
    def __init__(self, name, widget, x, y, event, w, h):

        self.button = QPushButton(widget)
        #self.button.initStyleOption('Blackadder ITC')
        self.button.setText(name)
        self.button.move(x, y)
        self.button.resize(int(W / w), int(H / h))
        self.button.setFont(QFont("Eras Demi ITC", (int(H / 60))))
        self.button.clicked.connect(event)

class Libri(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        Pagina(self, 'Libri')

        self.Label()

        self.line_edit = QLineEdit()

        self.createTable()

        self.Buttons()
        self.showMaximized()

    def Label(self):
        self.label1 = QLabel(self)
        self.label1.move(int(W/20), int(H/30))
        self.label1.setFont(QtGui.QFont(Font, int(H/10)))
        self.label1.setText("Lista di libri")

    def Buttons(self):
        self.indietro = Button("Indietro", self, int(W*3/4), int(H/22), self.Indietro, 7, 6)

    def createTable(self):
        LibriPrestati = LibriPossesso()
        Utenti = Users()
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(X_Y(Libreria)[0])
        self.tableWidget.setColumnCount(X_Y(Libreria)[1] + 3)

        self.tableWidget.setGeometry(int(H/2) - int(H/2), int(H/2), W - int(W/30), H - int(H/3))

        riga = 0
        colonna = 0
        Argomenti = ["ID Libro", "Titolo", "Autore", "Casa Editrice", "Scuola", "Proprietario", "Stato"]
        self.tableWidget.setHorizontalHeaderLabels(Argomenti)

        for x, item in Libreria.items():
            self.tableWidget.setItem(riga, colonna, QTableWidgetItem(x))
            colonna += 1
            self.tableWidget.setItem(riga, colonna, QTableWidgetItem(item['Titolo']))
            colonna += 1
            self.tableWidget.setItem(riga, colonna, QTableWidgetItem(item['Autore']))
            colonna += 1
            self.tableWidget.setItem(riga, colonna, QTableWidgetItem(item['Casa Editrice']))
            colonna += 1
            self.tableWidget.setItem(riga, colonna, QTableWidgetItem(item['Scuola']))
            colonna += 1
            self.tableWidget.setItem(riga, colonna, QTableWidgetItem(CodiceXNome(CodiceLXCodice(x, LibriPrestati), Utenti)))
            colonna += 1
            self.tableWidget.setItem(riga, colonna, QTableWidgetItem(GetStato(x, LibriPrestati)))
            colonna = 0
            riga += 1

        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        self.tableWidget.move(int(W/60), int(H/4))

    @pyqtSlot()
    def Indietro(self):
        self.app = App()
        self.app.show()
        self.close()

class RestituireLibro(QWidget):

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

class LibriInPossesso(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        Pagina(self, "Libri in possesso")

        self.Label()

        self.createTable()

        self.Buttons()

        self.showMaximized()

    def Label(self):
        self.label1 = QLabel(self)
        self.label1.move(int(W/20), int(H/30))
        self.label1.setFont(QtGui.QFont(Font, int(H/10)))
        self.label1.setText("Libri in possesso")


    def createTable(self):

        LibriPrestati = LibriPossesso()
        Utenti = Users()
        self.tableWidget = QTableWidget(self)

        self.tableWidget.setRowCount(X_Y(LibriPrestati)[0])
        self.tableWidget.setColumnCount(X_Y(LibriPrestati)[1])

        self.tableWidget.setGeometry(int(H/2) - int(H/2), int(H/2), W - int(W/30), H - int(H/3))
        riga = 0
        colonna = 0
        Argomenti = ["ID Prestito", "Libro", "Utente", "Data presa"]
        self.tableWidget.setHorizontalHeaderLabels(Argomenti)

        for x, item in LibriPrestati.items():
            if item['ID Utente'] == CurrentUser:
                if pd.isna(item['Data restituzione']):
                    self.tableWidget.setItem(riga, colonna, QTableWidgetItem(x))
                    colonna += 1
                    self.tableWidget.setItem(riga, colonna, QTableWidgetItem(CodiceXTitolo(item['ID Libro'], Libreria)))
                    colonna += 1
                    self.tableWidget.setItem(riga, colonna, QTableWidgetItem(CodiceXNome(item['ID Utente'], Utenti)))
                    colonna += 1
                    self.tableWidget.setItem(riga, colonna, QTableWidgetItem(item['Data presa']))
                    colonna = 0
                    riga += 1
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

        self.tableWidget.move(int(W/60), int(H/4))

    def Buttons(self):
        self.Indietro = Button("Indietro", self, int(W*3/4), int(H/22), self.Indietro, 7, 6)

    @pyqtSlot()
    def Indietro(self):
        self.app = App()
        self.app.show()
        self.close()

class PrendereInPrestito(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        Pagina(self, "Prendere in prestito")

        self.Label()

        self.Buttons()

        self.LineEdits()

        self.showMaximized()

    def Label(self):
        self.label = QLabel(self)
        self.label.move(int(W/20), int(H/30))
        self.label.setFont(QtGui.QFont(Font, int(H/10)))
        self.label.setText("Prendere in prestito")

    def LineEdits(self):
        self.CodiceLibro = QLineEdit(self)
        self.CodiceLibro.move(int(W/10), int(H*2/5))
        self.CodiceLibro.resize(int(W/3), int(H/20))

    def Buttons(self):
        self.indietro = Button("Indietro", self, int(W*3/4), int(H/22), self.Indietro, 7, 6)
        self.prendo = Button("prendere", self, int(W/3), int(H*7/15), self.Prendo, 10, 10)

    @pyqtSlot()
    def Indietro(self):
        self.app = App()
        self.app.show()
        self.close()

    @pyqtSlot()
    def Prendo(self):
        self.msg = QMessageBox(self)
        self.msg.setIcon(QMessageBox.Question)
        self.msg.setText("Sicuro di voler prendere questo libro?")
        self.msg.setWindowTitle("")
        self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        add("te", CurrentUser, "fsd")
class App(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        Pagina(self, "Hobby")

        self.Label()
        self.Buttons()

        self.showMaximized()

    def Label(self):
        self.label = QLabel(self)
        self.label.move(int(W/8), int(H/13))
        self.label.setFont(QtGui.QFont(Font, int(H/9)))
        self.label.setText("Benvenuti nella MiaLibreria")

    def Buttons(self):
        self.Button1 = Button("Libri", self, int(W/2) - int(W/17), int(H/2) - int(H/6), self.show_Libri, 8, 12)
        self.Button2 = Button("Libri in possesso", self, int(W/2) - int(W/17), int(H/2)-int(H/20), self.show_libriP, 8, 12)
        self.Button3 = Button("Restituire libro", self, int(W/4) - int(W/15), int(H*3/4) - int(H/7), self.show_libriR, 8 ,5)
        self.Button4 = Button("Prendere in prestito", self, int(W*3/4) - int(H/10), int(H*3/4) - int(H/7), self.show_PrendereInPrestito, 8, 5)


    def show_Libri(self):
        self.libri = Libri()
        self.libri.show()
        self.close()

    def show_libriR(self):
        self.libriR = RestituireLibro()
        self.libriR.show()
        self.close()

    def show_libriP(self):
        self.libriP = LibriInPossesso()
        self.libriP.show()
        self.close()

    def show_PrendereInPrestito(self):
        self.Prestito = PrendereInPrestito()
        self.Prestito.show()
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
    global Libreria
    Libreria = Biblioteca()
    global CurrentUser
    CurrentUser = "adex489"
    global Font
    Font = "CityBlueprint"
    Applicazione = App()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()