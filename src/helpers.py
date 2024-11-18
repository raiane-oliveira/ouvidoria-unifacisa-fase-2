def goBackToMenu():
    """Pergunta ao usuário se ele quer voltar ao menu ou encerrar o programa"""

    escolha = input("Pressione qualquer tecla para voltar ao menu, ou '7' para encerrar o programa:\n")
    return escolha


def getPositiveInteger(question = "Escolha a pergunta"):
    """Retorna um inteiro positivo válido e imprime 'Opção inválida' caso seja inválido"""

    numero = -1
    while numero < 1:
        entrada = input(question)

        if entrada.isdigit() and int(entrada) > 0:
            numero = int(entrada)
        else:
            print("Opção inválida. Tente novamente!\n")

    return numero