import os
from datetime import date

archivo = "expedientes.txt"
tipos = ["Matricula", "Constancia", "Certificado de estudios"]


def cargar():
    lista = []
    malas = []
    if os.path.exists(archivo):
        f = open(archivo, "r", encoding="utf-8")
        for linea in f:
            linea = linea.strip()
            if linea != "":
                partes = linea.split("|")
                ok = False
                if len(partes) == 6 and partes[0].split("-")[-1].isdigit():
                    ok = validar(partes[2], partes[3], partes[5])
                if ok:
                    lista.append(partes)
                else:
                    malas.append(linea)
        f.close()
    if len(malas) > 0:
        g = open("expedientes_danados.txt", "a", encoding="utf-8")
        for linea in malas:
            g.write(linea + "\n")
        g.close()
        print("Hay", len(malas), "lineas danadas")
        print("Se guardaron en expedientes_danados.txt")
    return lista


def guardar(lista):
    f = open(archivo, "w", encoding="utf-8")
    for exp in lista:
        f.write("|".join(exp) + "\n")
    f.close()


def validar(nombre, dni, asunto):
    if nombre == "" or asunto == "":
        return False
    if len(dni) != 8 or not dni.isdigit():
        return False
    return True