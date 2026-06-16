from rich import print
import time

class Livro:
    def __init__(self, titulo, pag):
        self.titulo = titulo
        self.total_paginas = pag
        self.pagina_atual = 1

        print(f":open_book: Você acabou de abrir o livro {self.titulo} que tem "
              f"{self.total_paginas} páginas no total. Você agora está na página"
              f" {self.pagina_atual}")

    def avancar_paginas(self,qtd = 1):
        cont = 0
        for pg in range (0, qtd, 1):
            if not self.fim_livro():
                self.pagina_atual += 1
                print(f"Pág {self.pagina_atual} :arrow_forward: ", end = '')
                time.sleep(0.4)
                cont += 1
        print(f"Você avançou {cont} páginas, e agora está na página {self.pagina_atual}")
        if self.fim_livro():
            print(f":closed_book: Você chegou ao final do livro {self.titulo}")

    def fim_livro(self) -> bool:
        return True if self.pagina_atual == self.total_paginas else False

l1 = Livro("Algo", 20)
l1.avancar_paginas(20)