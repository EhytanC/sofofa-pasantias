import math
sexo = input("C: crea archivo, E: existe archivo")
if sexo == "C":
    #Crea el archivo de texto
    Archivo = open("rut.txt","w")

#crea la variable rut donde se almacenara el rut del usuario y un string vacio para dar vuelta el rut y tener los digitos por separados
rut = input("Ingresa rut:")
rut_lista = []

#Se le ingresa el rut y rellena la lista vacia con los digitos del rut pero al inverso
def enlistar(rut_listado):  
    for i in reversed(rut_listado):
        rut_lista.append(i)

#Transforma todos las items de la lista a datos int
def parsearlista():
    enlistar(rut)
    for e in range(8):
        rut_lista[e] = int(rut_lista[e])

#Calcula el numero verificador usando la lista con los int
def calculo():
    parsearlista()
    suma = rut_lista[0]*2 + rut_lista[1]*3 + rut_lista[2]*4 + rut_lista[3]*5 + rut_lista[4]*6 + rut_lista[5]*7 + rut_lista[6]*2 + rut_lista[7]*3
    sumaR = suma / 11
    sumaR = math.trunc(sumaR) * 11
    sumaRes = suma - sumaR
    res = 11 - sumaRes
    if res == 10:
        num_ver = "k"
    elif res == 11:
        num_ver = 0
    else:
        num_ver = res
    return num_ver

#Llama a la funcion calculo para guardar el numero verificador en una variable y escribe en el archivo de texto el rut de la persona
def crearTxt():
    num_verificador = calculo()
    Archivo.write(str(rut)+"-"+str(num_verificador))
    Archivo.close()
crearTxt()
