import pandas as pd
import numpy
import os


def Users():
    #Aprire documento
    cartella = os.getcwd()
    os.chdir(cartella)

    Users = {}

    UsersP = pd.read_excel('FilesOperations\\a.xlsx', sheet_name='ListaUtenti')
    righe = UsersP.shape[0]
    numero = 0

    while numero < righe:
        Users[UsersP["ID"][numero]] = {"Nome": UsersP["NOME"][numero], "Cognome": UsersP["COGNOME"][numero], "Stato": UsersP["STATO"][numero]}
        numero += 1

    return Users

def UsersP():
    # Aprire documento
    cartella = os.getcwd()
    os.chdir(cartella)

    UsersP = pd.read_excel('FilesOperations\\a.xlsx')

    return UsersP

def printaS(spazio, dizionario):
    if spazio == "TUTTO":
        print(UsersP())
    else:
        for index, item in dizionario.items():
            print(index, item[spazio])

def NumeroItems(dizionario):
    numero = 0
    for x in dizionario:
        numero += 1
    return numero