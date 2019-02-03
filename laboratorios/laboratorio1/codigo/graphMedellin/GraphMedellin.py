from GraphALv2 import *

class GraphMedellin():

	"""
	Reprentacion en grafo de el mapa de la ciudad de medellin
	"""	

	def __init__(self, archivo, limitNodes, indexArcs, limitArchi):

		"""
		:param archivo: archivo con las coordenadas de la ciudad
		:param limitNodes: linea en la cual se encuentran las coordenadas del ultimo lugar ingresado
		:param indexArcs: comienzo de los arcos
		:param limitArchi: ultima linea del archivo
		"""
		self.__graph      = GraphALv2() 
		self.__limitNodes = limitNodes
		self.__indexArcs  = indexArcs
		self.__limitArchi = limitArchi
		self.__archivo 	  = open(archivo)
		self.__lista = self.__archivo.readlines()
	
	def makeNodes(self):

		"""
		Ingresa los nodos al grafo
		"""		

		for i in range(1, self.__limitNodes):

			line = self.__lista[i].split(" ")
			ids  = float(line[0])

			self.__graph.addNode(ids)


	def makeArcs(self):

		"""
		Ingresa los arcos al grafo
		"""

		print("")
		for i in range(self.__indexArcs, self.__limitArchi):

			line = self.__lista[i].split(" ")
			self.__graph.addArc(float(line[0]), float(line[1]), float(line[2]))


if __name__ == "__main__":

	graphd = GraphMedellin("medellin_colombia-grande.txt", 310154, 310156, 645944)
	graphd.makeNodes()
	graphd.makeArcs()









