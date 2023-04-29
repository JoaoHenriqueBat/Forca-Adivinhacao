import adivinha
import forca


def escolha_jogo():

    print("*********************************")
    print("********Escolha um jogo!*********")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Digite o número do jogo: "))

    if(jogo == 1):
        forca.jogar()
    elif(jogo == 2):
        adivinha.jogar()


if(__name__ == "__main__"):
    escolha_jogo()
