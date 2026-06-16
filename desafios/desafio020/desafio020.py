from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome,nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def add_favs(self, jogo):
        self.favoritos.append(jogo)
        self.favoritos = sorted(self.favoritos, key = str.lower)

    def status(self):
        conteudo = f"Nome real: {self.nome}"
        conteudo += f"\nJogos favoritos:"
        for num, game in enumerate(self.favoritos):
            conteudo += f"\n:video_game: {game}"
        painel = Panel (conteudo,title=f"Jogador {self.nick}", width=40)
        print(painel)

j1 = Gamer("Jogador 1", "Algo")
j1.add_favs("Mario")
j1.add_favs("Pokemon")
j1.add_favs("Sonic")

j1.status()