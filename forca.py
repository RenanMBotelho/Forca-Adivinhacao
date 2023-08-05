import jogos

import random

def jogar():

    imprime_mensagem_abertura()
    print("Categorias: [1] Animais / [2] Frutas / [3] Países\n")
    categoria = int(input("Escolha a categoria: "))
    print()
    inicio = 0

    while inicio == 0:
        if categoria == 1:
            inicio = 1
            palavra_secreta = carrega_palavra_secreta1()
        elif categoria == 2:
            palavra_secreta = carrega_palavra_secreta2()
            inicio = 1
        elif categoria == 3:
            palavra_secreta = carrega_palavra_secreta3()
            inicio = 1
        else:
            categoria = int(input("Escolha uma categoria válida: "))
            print()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print("O total de letras é", len(palavra_secreta))
    print()
    print(letras_acertadas)
    print("\n")
    enforcou = False
    acertou = False
    erros = 0
    limite_erros = 6
    tentativas = []

    while(not enforcou and not acertou):
        chute = pede_chute()

        if(chute not in tentativas and chute not in letras_acertadas):

            if(chute in palavra_secreta):
                marcar_chute_correto(chute, letras_acertadas, palavra_secreta)
                print("Tem a letra", chute)
                print()
                print("Letras enforcadas:", tentativas)
                print()
            else:
                erros += 1
                tentativas.append(chute)
                print("Você errou. Não tem {}. Total de erros: {} de {}\n".format(chute, erros, limite_erros))
                print("Letras enforcadas:", tentativas)
                desenha_forca(erros)

        else:
            print("Letra já digitada. Por favor, digite outra.\n")
            print("Letras enforcadas:", tentativas)
            print()

        enforcou = erros == limite_erros
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        print("\n")

    if(acertou):
        mensagem_vencedor()
    else:
        mensagem_perdedor(palavra_secreta)



def imprime_mensagem_abertura():
    print("\n**************************")
    print("Bem vindo ao jogo da Forca")
    print("**************************\n")

def carrega_palavra_secreta1():
    arquivo = open("lista animais.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def carrega_palavra_secreta2():
    arquivo = open("lista frutas.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def carrega_palavra_secreta3():
    arquivo = open("lista paises.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("\nQual a letra? ")
    print()
    chute = chute.strip().upper()
    return chute

def marcar_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def mensagem_vencedor():
    print("\n Parabéns, você ganhou! ")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       \n")
    finalizar = int(input("Pressione a tecla 1 para voltar ao menu inicial ou qualquer outra para sair: "))

    if finalizar == 1:
        print()
        jogos.menu_principal()
    else:
        input("Pressione qualquer tecla para finalizar")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      /|    ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
def mensagem_perdedor(palavra_secreta):
    print("Se enforcou! A palavra era {}\n".format(palavra_secreta))
    finalizar = int(input("Pressione a tecla 1 para voltar ao menu inicial ou qualquer outra para sair: "))

    if finalizar == 1:
        print()
        jogos.menu_principal()
    else:
        input("Pressione qualquer tecla para finalizar")

if(__name__ == "__main__"):
    jogar()