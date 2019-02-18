from Bfa2_0 import *

class N_Reinas:

    """
    This program calculates the positions in
    """

    def __init__(self, n):

        self.__count = 0
        self.__n = n
        self.__vector = []
        self.__solutions = []
        for i in range(0, n):
            self.__vector.append(i)

    def generatePermutations(self):

        pal = ""
        lis = Bfa2_0(self.__n)
        for i in self.__vector:
            pal = pal + str(i)

        lis.permutaciones(pal)
        listt = lis.getListt()
        for i in range(0, len(listt)):

            self.__vector = listt[i]

            for j in self.__vector:

                self.__vector[self.__vector.index(j)] = int(j)

            test = self.evaluate()

            if test:


                self.__count = self.__count + 1
                self.__solutions.append(self.__vector)

    def evaluate(self):

        value = False

        for i in range(0, self.__n):
            if i < self.__n - 1:
                for j in range(i+1, self.__n):
                    value = self.evaluateAux(i,
                                             self.__vector[i],
                                             j,
                                             self.__vector[j])

                    if value == False:
                        return value

        return value

    def evaluateAux(self, y1, x1, y2, x2):

        if abs(abs(y2) - abs(y1))\
                == abs(abs(x2) - abs(x1))\
                or abs(abs(y1) - abs(y2))\
                == abs(abs(x1) - abs(x2)):

            return False

        else:

            return True

    def getCount(self):

        print('numero de soluciones: '+str(self.__count))
        print('')
        print('Lista de todos los tableros que dan solucion: ')
        print(self.__solutions)


