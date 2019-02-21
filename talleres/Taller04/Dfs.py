"""
:Author: Santiago Espinosa Valderrama

"""

from GraphAL import *

class Dfs(GraphAL):

    """

    Esta clase hereda de la clase GraphAL
    Se encarga de evaluar en un grafo determinado si hay un camino posible entre un grafo
    de inicio y uno de finalización

    """

    def __init__(self, size):

        """
        constructor
        :param size: cantidad de nodos
        """

        super().__init__(size)

    def DfsEvaluate(self, source, destination):

        """

        :param source: Nodo de salida
        :param destination: Nodo de llegada
        :return: Boolean(True or False) si hay o no un camino que conduce de source a destination
        """

        if source == destination:

            return True


        else:

            for i in self.getSuccessors(source):

                if self.DfsEvaluate(i, destination):

                    return True


            return False


if __name__ == "__main__":

    test = Dfs(4)
    test.addArc(0, 2, 5)
    test.addArc(1, 0, 1)
    test.addArc(1, 1, 3)
    test.addArc(1, 2, 4)
    test.addArc(3, 0, 4)

    print(test.DfsEvaluate(2, 3))
