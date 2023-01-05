#Le pide usuario una frase y le quita todas las mayusculas
text = input("ingrese una frase: ")
text = text.lower()

#Listas que definen las letras legales e ilegales
abcdario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
vocales_tilde = ['á','é','í','ó','ú','-','_']

#Funcion que quita todos los signos de puntuacion
def remover():

    #Crea un string vacio para ingresar la frase hecha
    vacio = ""
    
    #El for revisa cada letra del texto
    for i in text:
    
        #Si pertenece al abcdario lo ingresa a la frase hecha
        if i in abcdario:
            vacio += i
    
        #Si encuentra los carateres con tilde o guiones los remplaza
        elif i in vocales_tilde:
            i = i.replace(vocales_tilde[0],"a")
            i = i.replace(vocales_tilde[1],"e")
            i = i.replace(vocales_tilde[2],"i")
            i = i.replace(vocales_tilde[3],"o")
            i = i.replace(vocales_tilde[4],"u")
            i = i.replace(vocales_tilde[5]," ")
            i = i.replace(vocales_tilde[6]," ")
            vacio += i
        else:
            pass
  
    #imprime en pantalla el string vacio el cual ya remplazo toda la frase    
    print(vacio + " <-- Este fue el resultado del string vacio")

remover()