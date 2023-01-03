palabra = str(input("ingresa palabra: "))
palabra = palabra.lower()
palabra = palabra.replace(" ","")
palabra = palabra.replace("á","a")
palabra = palabra.replace("é","e")
palabra = palabra.replace("í","i")
palabra = palabra.replace("ó","o")
palabra = palabra.replace("ú","u")
if palabra == palabra[::-1]:
    print("palindroma")
else:
    print("no palindroma")