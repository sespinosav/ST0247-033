class GraphAL:

    #La implementacion que haremos
    #se basa en una lista de diccionarios
    #donde el indice de la lista de los diccionarios
    #es el inicio
    #la llave del diccionario es el destino
    #y el peso es el valor de la llave en cada diccionario
    
    def __init__(self, size):
        
      #Creamos la lista
      self.__listt = []
       
      #Llenamos la lista con diccionarios vacios
      for i in range(size):
        self.__listt.append(dict())
      
    def addArc(self, vertex, edge, weight):
        
      #Agregamos una clave valor al diccionario ya existente
      #Que sera el inicio y el destino que conforma al arco nuevo
      self.__listt[vertex].update({edge : weight})


    def getSuccessors(self, vertice):
      
      #Retornamos una lista con las llaves de la lista
      #del diccionario, que vendrian siendo los nodos succesores
      return self.__listt[vertice].keys()

        
    def getWeight(self, source, destination):
       
      #Retornamos el peso del arco entre el inicio y el destino
      return self.__listt[source][destination]

    def __str__(self):

      pass
