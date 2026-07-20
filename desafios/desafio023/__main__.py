from poligono import *
from rich import inspect,print

def main():
    q = Quadrado(20)
    print(q.area())
    print(q.perimetro())

    c = Circulo(20)
    print(c.area())
    print(c.perimetro())
if __name__ == '__main__':
    main()