from rich import print, inspect

class Funcionario:
    empresa = "Curso em Vídeo"
    def __init__(self,nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        return (f":handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} "
                f"do setor de {self.setor} da empresa {Funcionario.empresa}")


c1 = Funcionario("Pedro", "Admnistração", "TI")
print(c1.apresentar())