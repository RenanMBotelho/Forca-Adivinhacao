import forca
import adivinhacao

def menu_principal():
    print("******************")
    print("Escolha o seu jogo")
    print("******************\n")

    print("(1) Forca / (2) Adivinhação\n")

    jogo = int(input("Escolha o jogo: "))

    if(jogo == 1):
        print("Jogo da Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogo da Adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    menu_principal()