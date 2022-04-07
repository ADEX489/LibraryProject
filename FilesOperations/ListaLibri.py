import pandas as pd
import numpy
import os


def Biblioteca():
    #Aprire documento
    cartella = os.getcwd()
    os.chdir(cartella)

    Biblioteca = {}

    BibliotecaP = pd.read_excel('C:\\Users\\ADEX_\\PycharmProjects\\pythonProject1\\FilesOperations\\a.xlsx')
    righe = BibliotecaP.shape[0]
    numero = 0

    while numero < righe:
        Biblioteca[BibliotecaP["CODICE ID"][numero]] = {"Titolo": BibliotecaP["TITOLO"][numero], "Autore": BibliotecaP["AUTORE"][numero], "Casa Editrice": BibliotecaP["CASA EDITRICE"][numero], "Scuola": BibliotecaP["SCUOLA"][numero]}
        numero += 1

    return Biblioteca

def BiblioP():
    # Aprire documento
    cartella = os.getcwd()
    os.chdir(cartella)

    BibliotecaP = pd.read_excel('C:\\Users\\ADEX_\\PycharmProjects\\pythonProject1\\FilesOperations\\a.xlsx')

    return BibliotecaP

def printaS(spazio, dizionario):
    if spazio == "TUTTO":
        print(BiblioP())
    else:
        for index, item in dizionario.items():
            print(index, item[spazio])

def X_Y(dizionario):
    righe = 0
    colonne = 0
    for x in dizionario:
        righe += 1
    for y in dizionario[x]:
        colonne += 1
    return [righe, colonne]
