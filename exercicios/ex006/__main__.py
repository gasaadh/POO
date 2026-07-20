from rich import print
from aluno import *
from funcionario import *
from professor import *

def main():
    a1 = Aluno('José', 17,'Informática','T01')
    a1.matricula()
    a1.aniversario()

if __name__ == '__main__':
    main()