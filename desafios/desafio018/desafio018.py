from rich import print
from rich.panel import Panel

class Churrasco:
    #Atributos de Classe
    consumo_padrao = 0.400
    preco_kg = 82.40

    def __init__(self, titulo, quant):
        # Atributos de instancia
        self.titulo = titulo
        self.participantes = quant

    def __str__(self):
        return f"Esse é {self.titulo} com {self.participantes} participantes"

    def calcular_qtd_carne(self) -> float:
        return self.participantes * Churrasco.consumo_padrao

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * self.__class__.preco_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.participantes

    def analisar(self):
        conteudo = f"Analisando {self.titulo} com {self.participantes} convidados"
        conteudo += (f"\nCada participante comerá {Churrasco.consumo_padrao}Kg e cada Kg"
                     f"custa R${Churrasco.preco_kg:.2f}")
        conteudo += (f"\nRecomendo comprar {self.calcular_qtd_carne():.3f}Kg de "
                     f"carne")
        conteudo += f"\nO custo total será de R${self.calcular_custo_total():.2f}"
        conteudo += f"\nCada pessoa pagará R${self.calcular_custo_individual():.2f}"
        painel = Panel(conteudo, title=self.titulo)
        print(painel)
        
c1 = Churrasco("Churras", 15)
c1.analisar()