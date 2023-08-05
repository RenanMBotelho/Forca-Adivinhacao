import jogos

def jogar():

    import random

    print("\n*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************\n")

    total_tentativas = 0
    numero_minimo = 1
    numero_maximo = 100
    pontos = 100
    #random.seed(100) #função Seed: dá o ponto de partida para a escolher aleatória do número
    numero_secreto = random.randrange(numero_minimo,numero_maximo + 1)
    inicio = 0

    print("Qual o nível de dificuldade?")
    print("(1) Fácil / (2) Médio / (3) Difícil")

    nivel=int(input("Digite o nível: "))
    print()

    while inicio == 0:
        if(nivel == 1):
            inicio = 1
            total_tentativas = 9
        elif(nivel == 2):
            inicio = 1
            total_tentativas = 7
        elif(nivel == 3):
            inicio = 1
            total_tentativas = 5
        else:
            nivel = int(input("Escolha um nível válido: "))
            print()

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute_str = input("Digite um número entre {} e {}: ".format(numero_minimo, numero_maximo))
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < numero_minimo or chute > numero_maximo):
            print("Número inválido. Você deve digitar um número entre {} e {}!\n".format(numero_minimo, numero_maximo))
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("\nVOCÊ ACERTOU!\n")
            break
        else:
            if(maior):
                print("Você ERROU! Seu chute foi MAIOR que o número secreto.\n")
            elif(menor):
                print("Você ERROU! Seu chute foi MENOR que o número secreto.\n")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo! O número secreto é: {}. Pontuação total: {}\n".format(numero_secreto,pontos))
    finalizar = int(input("Pressione a tecla 1 para voltar ao menu inicial ou qualquer outra para sair: "))

    if finalizar == 1:
        print()
        jogos.menu_principal()
    else:
        input("Pressione qualquer tecla para finalizar")

if(__name__ == "__main__"):
    jogar()