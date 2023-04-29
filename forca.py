import random


def jogar():
    print("*"*33)
    print("Bem vindo ao jogo da forca!".center(33, "*"))
    print("*"*33)

    arquivo = open(r"C:\Users\João Henrique\Desktop\Alura\Python\jogos\palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip().upper())
    arquivo.close()

    n = random.randrange(0, len(palavras))
    palavra_secreta = palavras[n]
    letras_acertadas = ["_" for letra in palavra_secreta]
    index = 0
    for letra in palavra_secreta:
        if " " == letra:
            letras_acertadas[index] = "-"
        index += 1
    tentativas = 0
    erros = 0

    enforcou = False
    acertou = False

    print("Escolha a dificuldade:\n(1) Fácil (2) Médio (3) Difícil")
    dificuldade = int(input(""))

    if dificuldade == 1:
        tentativas = 15
    elif dificuldade == 2:
        tentativas = 10
    else:
        tentativas = 5

    while(not enforcou and not acertou):

        print("=-="*11)
        print(letras_acertadas)

        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()

        if len(chute) > 1:
            print("Digite apenas 1 letra!")
            continue

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra.upper():
                    print(f"Você descobriu a letra {chute}",
                          f"na posição {index}")
                    letras_acertadas[index] = letra.upper()
                index += 1
        else:
            erros += 1
        enforcou = erros == tentativas
        acertou = letras_acertadas.count("_") == 0
        print(f"{erros} erros de {tentativas}")

    if acertou:
        print(f"Parabéns você acertou, palavra secreta: {palavra_secreta}")
    elif enforcou:
        print(f"Você enforcou, palavra secreta: {palavra_secreta}")
    print("Fim do jogo")


if(__name__ == "__main__"):
    jogar()
