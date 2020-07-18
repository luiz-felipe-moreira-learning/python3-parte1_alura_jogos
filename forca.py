import random

def jogar():
    print("**************************")
    print("Bem vindo ao jogo de Forca")
    print("**************************")

    print("Fim do jogo")

    palavra_secreta = "python"

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        index = 0
        chute = input("Qual a letra? ")
        chute = chute.strip()
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1
        print("jogando...")

if (__name__ == "__main__"):
    print("Jogando forca")
    jogar()