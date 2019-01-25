class GraphAL:

    #La implementacion que haremos
    #se basa en una lista de tuplas
    #de diccionarios
    #donde el indice de la lista de las tuplas
    #es el inicio 
    #la llave del diccionario es el destino
    #y el peso es el valor del diccionario

    def __init__(self, size):
      self.__listt = []

      for i in range(size):
        self.__listt.append(dict())
      
    def addArc(self, vertex, edge, weight):

      self.__listt[vertex].update({edge : weight})


    def getSuccessors(self, vertice):

      return self.__listt[vertice].keys()

        
    def getWeight(self, source, destination):

      return self.__listt[source][destination]

    def __str__(self):

      pass
