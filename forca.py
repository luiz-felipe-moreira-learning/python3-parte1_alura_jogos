import random

def jogar():
    print("**************************")
    print("Bem vindo ao jogo de Forca")
    print("**************************")

    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip("\n")
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    while (not enforcou and not acertou):
        index = 0
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()
        if (chute in palavra_secreta):
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            erros += 1
        acertou = "_" not in letras_acertadas
        enforcou = erros == 6
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!")
    else:
        print("você perdeu!")
    print("Fim do jogo")


if (__name__ == "__main__"):
    print("Jogando forca")
    jogar()