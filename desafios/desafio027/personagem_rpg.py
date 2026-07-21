import random
from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca=100):
        if self.vida > 0 and alvo.vida >0:
            golpe = self.golpes[random.randint(0,len(self.golpes))]

            print(f'{self.nome} ({self.vida}) atacou {alvo.nome} ({alvo.vida}) com um {golpe} de força {forca}')
            alvo.receber_dano(forca)
        else:
            print(f"O ataque {self.nome} -> {alvo.nome} não pode acontecer")


    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        self.vida -= fator
        if self.vida <= 0:
            self.vida = 0
        print(f"{self.nome} recebeu dano de {fator}")

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Soco","Tapa","Mordida"]

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f'{self.nome} enrolou uma atadura nos ferimentos e recuperou {fator} pontos de vida')

class Mago(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Magia","Raio de Luz","Bola de Fogo"]

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f'{self.nome} fez uma magia de cura e curou {fator} pontos de vida')


