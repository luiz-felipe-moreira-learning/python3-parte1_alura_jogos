import random

def jogar():
    print("**************************")
    print("Bem vindo ao jogo de Forca")
    print("**************************")

    print("Fim do jogo")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)
    while (not enforcou and not acertou):
        index = 0
        chute = input("Qual a letra? ")
        chute = chute.strip()
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1
        print(letras_acertadas)

if (__name__ == "__main__"):
    print("Jogando forca")
    jogar()