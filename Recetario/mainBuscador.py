import pandas as pd

df_rec = pd.read_csv('db/recipes.csv', index_col="id")
df_ing = pd.read_csv('db/ingredients.csv', index_col="id")
df_itr = pd.read_csv('db/ingredients_recipes.csv')

varSlt = ""
def alfaNumerico(varAlf):
    abc=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','ñ']
    for i in varAlf:
        if i in abc:
            return False
    return True

def buscadorReceta(nombreRec):
    resultado_fil = df_rec[df_rec["name"].str.contains(nombreRec)]
    return resultado_fil

def buscarIngredientes(idRec):
    allIng=[]
    varId = df_itr[df_itr["recipe_id"] == idRec]
    varId = list(varId.ingredient_id.values)
   
    for i in range(len(varId)):
         ingredientes = df_ing.loc[varId[i]]['name']
         allIng.append(ingredientes)
    return allIng

while varSlt != "salir":
    print("\n-Buscador de rectas")
    print('Escribe "salir" para finalizar el programa \n')
    varSlt = input("Ingresa palabras clave: ")
    
    if varSlt != "salir":
        print("Resultados:")
        resultadoBusqueda = buscadorReceta(varSlt)
        
        if resultadoBusqueda.empty:
            print("No se encontraron recetas")
        else:
            print(resultadoBusqueda["name"].head())
            
            while varSlt != "N":
                varSlt = input("\nQuieres inspeccionar una de las recetas? Y/N: ")
                varSlt = varSlt.upper()
            
                if varSlt == "Y":
                    listaIngredientes = []
                    
                    while listaIngredientes == []:
                        varSlt = input("\nIngrese ID de la receta que desea seleccionar: ")
                        if listaIngredientes == [] and varSlt != '' and varSlt != 'salir' and alfaNumerico(varSlt):
                            listaIngredientes = buscarIngredientes(int(varSlt))
                            print("\nLos ingredientes de "+ str(resultadoBusqueda.loc[int(varSlt)]["name"])+" son: ")   
                            print(listaIngredientes)
                            print("\nReceta: "+ str(resultadoBusqueda.loc[int(varSlt)]["description"]))
                            varSlt = "N"
                        elif varSlt == 'salir':
                            exit()
                elif varSlt == "SALIR":
                    exit()