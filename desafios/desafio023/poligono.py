import math
from abc import ABC, abstractmethod


class Poligono(ABC):

    def __init__(self,lados):
        self.qtd_lados = lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Quadrado(Poligono):

    def __init__(self,lados = 1):
        super().__init__(4)
        self.lados = lados

    def perimetro(self):
        return self.lados * 4

    def area(self):
        return self.lados ** 2

class Circulo(Poligono):
    def __init__(self,raio = 1):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        return 2 * math.pi * self.raio

    def area(self):
        return math.pi * (self.raio ** 2)