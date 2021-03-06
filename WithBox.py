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
        Argomenti = ["ID Libro", "Titolo", "Autore", "Casa Editrice", "Scuola", "In prestito da", "Anno", "Materia", "Stato", "Disponibilita"]
        self.tableWidget.setHorizontalHeaderLabels(Argomenti)

        for x, item in Libreria.items():
            self.tableWidget.setItem(riga, colonna, QTableWidgetItem(x))
            colonna += 1
            self.tableWidget.setItem(riga, colonna, QTableWidgetItem(NANxVOID(item['Titolo'])))
            colonna += 1
            self.tableWidget.setItem(riga, colonna, QTableWidgetItem(NANxVOID(item['Autore'])))
            colonna += 1
            self.tableWidget.setItem(riga, colonna, QTableWidgetItem(NANxVOID(item['Casa Editrice'])))
            colonna += 1
            self.tableWidget.setItem(riga, colonna, QTableWidgetItem(NANxVOID(item['Scuola'])))
            colonna += 1
            self.tableWidget.setItem(riga, colonna, QTableWidgetItem(NANxVOID(CodiceXNome(CodiceLXCodice(x, LibriPrestati), Utenti))))
            colonna += 1
            self.tableWidget.setItem(riga, colonna, QTableWidgetItem(str(int(item['Anno']))))
            colonna += 1
            self.tableWidget.setItem(riga, colonna, QTableWidgetItem(NANxVOID(item['Materia'])))
            colonna += 1
            self.tableWidget.setItem(riga, colonna, QTableWidgetItem(NANxVOID(item['Stato'])))
            colonna += 1
            self.tableWidget.setItem(riga, colonna, QTableWidgetItem(NANxVOID(GetStato(x, LibriPrestati))))
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

        self.createTable()

        self.CodicePrestito = QLineEdit(self)
        self.CodicePrestito.move(int(W*7/12), int(H * 2 / 5))
        self.CodicePrestito.resize(int(W / 3), int(H / 20))

        self.prendo = QPushButton(self)
        self.prendo.setText("Restituire")
        self.prendo.move(int(W*9/11), int(H * 7 / 15))
        self.prendo.resize(int(W / 10), int(H / 10))
        self.prendo.setFont(QFont("Eras Demi ITC", (int(H / 60))))
        self.prendo.clicked.connect(self.Restituisco)

        self.showMaximized()

    def Label(self):
        self.label = QLabel(self)
        self.label.move(int(W/20), int(H/30))
        self.label.setFont(QtGui.QFont(Font, int(H/10)))
        self.label.setText("Libri da restituire")

    def createTable(self):

        LibriPrestati = LibriPossesso()
        Utenti = Users()
        self.tableWidget = QTableWidget(self)

        self.tableWidget.setRowCount(X_Y(LibriPrestati)[0])
        self.tableWidget.setColumnCount(X_Y(LibriPrestati)[1]-1)

        self.tableWidget.setGeometry(int(W / 2) - int(W / 3), int(H / 5), W - int(W*4/7), H - int(H / 2))
        riga = 0
        colonna = 0
        Argomenti = ["ID Prestito", "Libro", "Data presa"]
        self.tableWidget.setHorizontalHeaderLabels(Argomenti)

        for x, item in LibriPrestati.items():
            if item['ID Utente'] == CurrentUser:
                if pd.isna(item['Data restituzione']):
                    self.tableWidget.setItem(riga, colonna, QTableWidgetItem(str(x)))
                    colonna += 1
                    self.tableWidget.setItem(riga, colonna, QTableWidgetItem(CodiceXTitolo(item['ID Libro'], Libreria)))
                    colonna += 1
                    self.tableWidget.setItem(riga, colonna, QTableWidgetItem(str(item['Data presa'])))
                    colonna = 0
                    riga += 1
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

        self.tableWidget.move(int(W / 60), int(H / 3))

    def Buttons(self):
        self.Indietro = Button("Indietro", self, int(W*3/4), int(H/22), self.Indietro, 7, 6)

    @pyqtSlot()
    def Indietro(self):
        self.app = App()
        self.app.show()
        self.close()

    @pyqtSlot()
    def Restituisco(self):
        codice = self.CodicePrestito.text()
        if int(codice) in LibriPossesso():
            if CodiceinA(int(codice)) == 1:
                self.msg = QMessageBox()
                self.msg.setText("Stai restituendo il libro giusto?")
                self.msg.setWindowTitle("Domanda di controllo")
                self.msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                ret = self.msg.exec();
                if ret == QMessageBox.Yes:
                    AggDataRitorno(int(codice))
                    Esiste = QMessageBox()
                    Esiste.setIcon(QMessageBox.Information)
                    Esiste.setText("Restituito con successo")
                    Esiste.setWindowTitle("Congratulazioni!")
                    Esiste.setStandardButtons(QMessageBox.Ok)
                    retval = Esiste.exec_()
            else:
                NonEsiste = QMessageBox()
                NonEsiste.setIcon(QMessageBox.Warning)
                NonEsiste.setText("Il libro risulta restituito")
                NonEsiste.setWindowTitle("Errore controllo libri")
                NonEsiste.setStandardButtons(QMessageBox.Ok)
                retval = NonEsiste.exec_()

        else:
            NonEsiste = QMessageBox()
            NonEsiste.setIcon(QMessageBox.Warning)
            NonEsiste.setText("Non ho trovato quel libro")
            NonEsiste.setWindowTitle("Errore controllo libri")
            NonEsiste.setStandardButtons(QMessageBox.Ok)
            retval = NonEsiste.exec_()

class LibriInPossesso(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        Pagina(self, "Libri prestati")

        self.Label()

        self.createTable()

        self.Buttons()

        self.showMaximized()

    def Label(self):
        self.label1 = QLabel(self)
        self.label1.move(int(W/20), int(H/30))
        self.label1.setFont(QtGui.QFont(Font, int(H/10)))
        self.label1.setText("Libri in prestito")


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
                    self.tableWidget.setItem(riga, colonna, QTableWidgetItem(str(x)))
                    colonna += 1
                    self.tableWidget.setItem(riga, colonna, QTableWidgetItem(CodiceXTitolo(item['ID Libro'], Libreria)))
                    colonna += 1
                    self.tableWidget.setItem(riga, colonna, QTableWidgetItem(CodiceXNome(item['ID Utente'], Utenti)))
                    colonna += 1
                    self.tableWidget.setItem(riga, colonna, QTableWidgetItem(str(item['Data presa'])))
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

        self.CodiceLibro = QLineEdit(self)
        self.CodiceLibro.move(int(W/10), int(H*2/5))
        self.CodiceLibro.resize(int(W/3), int(H/20))

        self.indietro = Button("Indietro", self, int(W*3/4), int(H/22), self.Indietro, 7, 6)

        self.prendo = QPushButton(self)
        self.prendo.setText("prendere")
        self.prendo.move(int(W/3), int(H*7/15))
        self.prendo.resize(int(W / 10), int(H / 10))
        self.prendo.setFont(QFont("Eras Demi ITC", (int(H / 60))))
        self.prendo.clicked.connect(self.Prendo)

        self.showMaximized()

    def Label(self):
        self.label = QLabel(self)
        self.label.move(int(W/20), int(H/30))
        self.label.setFont(QtGui.QFont(Font, int(H/10)))
        self.label.setText("Prendere in prestito")

    @pyqtSlot()
    def Indietro(self):
        self.app = App()
        self.app.show()
        self.close()

    @pyqtSlot()
    def Prendo(self):
        if self.CodiceLibro.text() in Libreria:
            codice = self.CodiceLibro.text()

            self.msg = QMessageBox()
            self.msg.setText("Sicuro di voler prendere questo libro?")
            self.msg.setWindowTitle("Domanda di controllo")
            self.msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            ret = self.msg.exec();
            if ret == QMessageBox.Yes:
                add(codice, CurrentUser)
                Esiste = QMessageBox()
                Esiste.setIcon(QMessageBox.Information)
                Esiste.setText("Preso con successo")
                Esiste.setWindowTitle("Congratulazioni!")
                Esiste.setStandardButtons(QMessageBox.Ok)
                retval = Esiste.exec_()

        else:
            NonEsiste = QMessageBox()
            NonEsiste.setIcon(QMessageBox.Warning)
            NonEsiste.setText("Non ho trovato quel libro")
            NonEsiste.setWindowTitle("Errore controllo libri")
            NonEsiste.setStandardButtons(QMessageBox.Ok)
            retval = NonEsiste.exec_()

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
        self.Button2 = Button("Libri prestati", self, int(W/2) - int(W/17), int(H/2)-int(H/20), self.show_libriP, 8, 12)
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

def UserLog():
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
    UserLog()