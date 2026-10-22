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


def elegir_tipo():
    for i in range(len(tipos)):
        print(i + 1, "-", tipos[i])
    op = input("Tipo de tramite: ")
    while not op.isdigit() or int(op) < 1 or int(op) > len(tipos):
        op = input("Opcion no valida, elige otra vez: ")
    return tipos[int(op) - 1]


def mostrar(exp):
    print("Codigo:", exp[0])
    print("Fecha:", exp[1])
    print("Nombre:", exp[2])
    print("DNI:", exp[3])
    print("Tipo:", exp[4])
    print("Asunto:", exp[5])
    print("--------------------")


def registrar(lista):
    valido = False
    while valido == False:
        nombre = input("Nombre: ").strip().replace("|", "-")
        dni = input("DNI: ").strip()
        tipo = elegir_tipo()
        asunto = input("Asunto: ").strip().replace("|", "-")
        valido = validar(nombre, dni, asunto)
        if valido == False:
            print("Datos invalidos, intente de nuevo")
    mayor = 0
    for exp in lista:
        numero_exp = int(exp[0].split("-")[-1])
        if numero_exp > mayor:
            mayor = numero_exp
    numero = mayor + 1
    codigo = "EXP-" + str(date.today().year) + "-" + str(numero).zfill(4)
    fecha = str(date.today())
    nuevo = [codigo, fecha, nombre, dni, tipo, asunto]
    lista.append(nuevo)
    guardar(lista)
    print("Expediente registrado:", codigo)
    

def buscar(lista):
    codigo = input("Codigo a buscar: ").strip().upper()
    encontrado = False
    i = 0
    while i < len(lista) and encontrado == False:
        if lista[i][0] == codigo:
            mostrar(lista[i])
            encontrado = True
        i = i + 1
    if encontrado == False:
        print("Expediente no encontrado")


def listar(lista):
    if len(lista) == 0:
        print("No hay expedientes")
    for exp in lista:
        mostrar(exp)

PARTE 4 → mensaje del commit: agrega ordenar

def ordenar(lista):
    print("1. Por fecha")
    print("2. Por nombre")
    op = input("Opcion: ").strip()
    if op == "1":
        pos = 1
    elif op == "2":
        pos = 2
    else:
        print("Opcion no valida")
        return
    hubo_cambio = True
    while hubo_cambio == True:
        hubo_cambio = False
        for i in range(len(lista) - 1):
            if lista[i][pos].lower() > lista[i + 1][pos].lower():
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                hubo_cambio = True
    guardar(lista)
    listar(lista)
