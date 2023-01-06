a = input('--')
print(a)
import pandas as pd
import datetime from datetime

def agregar_receta(df_recetas, ingredientes, descripcion):
    # id,"name","description",user_id,"created_at","updated_at"  LLAVES
    nueva_receta = {
        'ingredientes': ingredientes, 
        'descripcion': descripcion
    }
    df_receta = pd.DataFrame(nueva_receta)
    df_recetas.append(df_receta)
    return df_recetas