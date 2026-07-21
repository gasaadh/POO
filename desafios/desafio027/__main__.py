from personagem_rpg import *

def main():
    g1 = Guerreiro("Homem", 100)
    g2 = Mago("Mago", 200)

    g1.atacar(g2, 100)
    g2.atacar(g1, 100)

if __name__ == "__main__":
    main()