import numpy as np

#Ejercicios de la materia estructura de datos.
#Son ejercicios de distintas practicas, por ende no hay relacion entre ellos.


'''
Implementa el TDA "Quiniela" que modela un juego de quiniela con dos números premiados. La estructura contiene:

Primer número premiado
Segundo número premiado
Multiplicador (cuánto se paga por cada peso apostado)
Implementar las siguientes operaciones:

Constructor: Debe incluir las validaciones necesarias, teniendo en cuenta que los números que participan se encuentran entre 0 y 999.
__repr__: Al usar la función print con una variable del tipo quiniela debe mostrar: Primer número ganador: 'numero' - Segundo número ganador: 'numero' - Paga: 'multiplicador'X.

esNumeroGanador: Operación que recibe un número por parámetros y retorna True 
  si el número resultó ganador o False en caso contrario.

importeAPagar: Operación que recibe un número y el monto apostado por parámetros y retorna el 
  importe a pagar si la apuesta es ganadora o 0 en caso contrario. Si el número es el primer premio, 
  se paga 'mutiplicador' por cada peso apostado, si es el segundo premio se paga la mitad. 
  Solo se aceptan apuestas hasta $1000.

premiadosCercanos: Operación que retorna True si los números premiados están a menos
 de 10 números de distancia y False en caso contrario.

'''

class Quiniela:
  def __init__(self, primerPremiado, segPremiado, multiplicador):
    if 0 <= primerPremiado <= 999 : self.primerPremiado = primerPremiado 
    else: raise(Exception("El numero debe estar entre 0 y 999"))

    if 0 <= segPremiado <= 999 : self.segPremiado = segPremiado 
    else: raise(Exception("El numero debe estar entre 0 y 999"))

    self.multiplicador = multiplicador

  def __repr__(self):
    return f"Primer numero ganador:{self.primerPremiado} - Segundo numero ganador: {self.segPremiado} - Paga {self.multiplicador}X"
  
  def esNumeroGanador(self,num):
    return num == self.primerPremiado or num == self.segPremiado
  
  def importeAPagar(self,num,montoApostado):
    if montoApostado > 1000:
      raise(Exception("Solo se aceptan apuestas hasta $1000"))

    if num == self.primerPremiado :
      return montoApostado * self.multiplicador
    elif num == self.segPremiado:
      return montoApostado * self.multiplicador / 2
    else:
      return 0
    
  def premiadosCercanos(self):
    distancia = abs(self.primerPremiado - self.segPremiado)
    return distancia < 10




def busquedaLineal(arr,n):   
  """Busca el indice del elemento *n* en el vector *arr* de forma lineal.

  
  Args:
      arr (list of int): arreglo a recorrer . puede ser de tipo list o numpy.array
      n (int): elemento del cual se buscara el indice

  Returns: 
    list: indice del elemento *n*
  """
  indice = 0
  for i in range(len(arr)):
      if arr[i] == n:
            indice = i
  return indice


    

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