from funcionarios import *
from rich import inspect

def main():
    f1 = FuncionarioHorista("José",45)
    f1.calcular_salario()
    f1.analisar_salario()

if __name__ == "__main__":
    main()