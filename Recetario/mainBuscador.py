import pandas as pd

df_rec = pd.read_csv('recipes.csv', index_col="id")
df_ing = pd.read_csv('ingredients.csv', index_col="id")
df_itr = pd.read_csv('ingredients_recipes.csv')
varSlt = ""

def buscadorReceta(nombreRec):
    resultado_fil = df_rec[df_rec["name"].str.contains(nombreRec)]
    return resultado_fil

def buscarIngredientes(idRec):
    allIng=[]
    varId = df_itr[df_itr["recipe_id"] == idRec]
    varId = list(varId.ingredient_id.values)
   
    for i in range(len(varId)):
         ingredientes = df_ing.iloc[varId[i]]['name']
         allIng.append(ingredientes)
    return allIng

while varSlt != "salir":
    print("\n-Buscador de rectas")
    print('Escribe "salir" para finalizar el programa \n')
    varSlt = input("Ingresa palabras clave: ")
    
    if varSlt != "salir":
        print("Resultados:")
        resultadoBusqueda = buscadorReceta(varSlt)
        print(resultadoBusqueda["name"].head())
    
        while varSlt != "N":
            varSlt = input("\nQuieres inspeccionar una de las recetas? Y/N: ")
            varSlt = varSlt.upper()
    
            if varSlt == "Y":
                varSlt = int(input("\nIngrese ID de la receta que desea seleccionar: "))
                print("\nLos ingredientes de "+ str(resultadoBusqueda.loc[varSlt]["name"])+" son: ")
                print(buscarIngredientes(varSlt))
                print("\nReceta: "+ str(resultadoBusqueda.loc[varSlt]["description"]))
                varSlt = "N"
    
            elif varSlt == "SALIR":
                exit()