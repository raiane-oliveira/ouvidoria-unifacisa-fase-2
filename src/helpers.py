"""
def goBackToMenu():
    # Pergunta ao usuário se ele quer voltar ao menu ou encerrar o programa

def getPositiveInteger():
    # Retorna um inteiro positivo válido e imprime 'Opção inválida' caso seja inválido
"""

def goBackToMenu():
    escolha = input("Pressione qualquer tecla para voltar ao menu, ou '7' para encerrar o programa:\n")
    return escolha


def getPositiveInteger(question = "Escolha a pergunta"):
    numero = -1
    while numero < 1:
        entrada = input(question)

        if entrada.isdigit() and int(entrada) > 0:
            numero = int(entrada)
        else:
            print("Opção inválida. Tente novamente!\n")

    return numero

"""
Exemplo de como Usar
pergunta_usuario = input("Qual pergunta você quer usar para o usuário? ")
resultado = getPositiveInteger(question=pergunta_usuario)
print(f"Você digitou: {resultado}")
"""