#Funcion que crea una lista que agrega los elementos de forma en espiral apartir de una matriz
def getSpiralMatrix(inputMatrix):

	#Crea la lista vacia
	resultado = []

	#Si la lista viene vacia retorna la lista vacia
	if len(inputMatrix)==0:
		return resultado

	#Declara las variables que tienen la primera fila y columna, y la ultima fila y columna
	fil_inicio = 0
	fil_fin = len(inputMatrix) - 1
	col_inicio = 0
	col_fin = len(inputMatrix[0]) - 1

	#Mientras que la fila de partida sea menor o igual a la fila de termino sigue el bucle y lo mismo para las columnas
	while fil_inicio <= fil_fin and col_inicio <= col_fin:
		#i parte desde la columna de inicio y se detiene en la columna final, mientras que en todo su recorrido va agregando los items que esten en la fila que guarde la variable
		for i in range(col_inicio, col_fin+1):
			resultado.append(inputMatrix[fil_inicio][i])

		#le suma a la fila de inicio porque ya no se debe ocupar la fila que acaba de ser leida
		fil_inicio += 1
		
		#e parte desde la file de inicio y se detiene en la columna final, mientras que en todo su recorrido va agregando los items que esten en la columna que guarde la variable
		for e in range(fil_inicio,fil_fin+1):
			resultado.append(inputMatrix[e][col_fin])
		
		#Le resta a la columna final para no leer la columna que acaba de ser leida
		col_fin -= 1

		#Si la fila de inicio es menor o igual a la de fin entonces...	
		if fil_inicio <= fil_fin:
		
			#i utiliza la ultima fila y empieza a recorrerla al inverso y agregando todos los items que recorre
			for i in range(fil_fin, fil_inicio-1,-1):
				resultado.append(inputMatrix[fil_fin][i])
		
		#le resta -1 a la columna final para que no se repita la fila que acaba de agregar
		fil_fin -= 1
		
		#Si la columna de inicio es menor o igual a la de fin entonces...
		if col_inicio <= col_fin:
		
			#i empieza a agregar todos los itmems en el recorrido que hay entre la columna de fin a la columna de inicio
			for i in range(col_fin,col_inicio-1,-1):
				resultado.append(inputMatrix[i][col_inicio])
		
		#le resta -1 a la fila inicial para que no se repita la fila que acaba de agregar
		col_inicio +=1

		#retorna la lista en espiral ordenada
	return resultado

matrix = [
	[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
print(getSpiralMatrix(matrix))