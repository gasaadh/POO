from exercicios.ex009.ex009 import Avaliacao
from rich import print, inspect

def main():
    av1 = Avaliacao("Pedro","Matemáatica",9.5)
    av1.set_nota(10)
    print(f"{av1.nome} tirou {av1.get_nota()}")
    inspect(av1, private=True)

if __name__ == '__main__':
    main()
