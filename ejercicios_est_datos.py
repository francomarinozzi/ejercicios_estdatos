import numpy as np

#Ejercicios de la materia estructura de datos.
#Son ejercicios de distintas practicas, por ende no hay relacion entre ellos.

def busquedaBinaria(lista,elem, i, j ): 
  """ Busca el indice de *elem* en *lista*, implementando la busqueda binaria de manera recursiva.  
      

  Args:
      lista (list): lista en la que se buscara *elem*
      elem (int): elemento a buscar su indice
      i (int): indice inicial de la busqueda
      j (int): indice final de la busqueda

  Returns:
      int: indice de *elem* en la lista. (Si el elemento no se encuentra en la lista, devuelve -1)
  """
  if i > j:
      return -1
  medio = (i + j )// 2
  if lista[medio] == elem:
      return medio
  elif lista[medio] < elem:  
      return busquedaBinaria(lista, elem, medio +1 , j)
  else:
      return busquedaBinaria(lista, elem, i, medio -1)



def inversionRecursiva(cadena): 
    """Funcion recursiva que recibe por parametro un string y lo devuelve invertido

    Args:
        cadena (str): string a invertir

    Returns:
        str: *cadena* invertido
    """
    nuevoString = ""
    if len(cadena) == 1:
        nuevoString = cadena
    else:
        nuevoString = cadena[-1] + inversionRecursiva(cadena[:-1])
    return nuevoString




def sumaVect(arr):
    """función recursiva que recibe un vector como parámetro y retorna la suma de todos sus elementos.

    Args:
        arr (list of int): lista de la cual se sumaran los elementos

    Returns:
        int: suma de todos los elementos de *arr*
    """
    sum = 0
    if len(arr) == 1:
        sum += arr[0]
    else:
        sum += arr[-1] + sumaVect((arr[:-1]))
    return sum




def matrizDiagonal(matriz): 
    """ Recibe una matriz cuadrada de números reales (N x N) por parámetro y calcula la suma de los elementos que están por encima de la diagonal principal (excluyendo la diagonal).
        por ej, si la matriz es:
        [1,2,3]
        [4,5,6]
        [7,8,9]
        debe devolver 11 (2 + 3 + 6)

    PRE: *matriz* Debe ser de NxN
    Args:
        matriz (numpy array): matriz a sumar.

    Returns:
        int: suma de los numeros por encima de la diagonal de *matriz*
    """
    
    sum = 0
    for fila in range(len(matriz)):

        for elem in range(fila + 1,len(matriz[fila])):
            sum += matriz[fila][elem]
            print(sum)
    return sum
