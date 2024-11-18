"""
def goBackToMenu():
    # Pergunta ao usuário se ele quer voltar ao menu ou encerrar o programa

def getPositiveInteger():
    # Retorna um inteiro positivo válido e imprime 'Opção inválida' caso seja inválido
"""

def goBackToMenu():
    escolha = -1
    while escolha != 2:
        print("1) Voltar ao menu principal\n2) Encerrar o programa de Ouvidoria")
        if escolha == 1:
            print("Voltando ao menu principal")
        elif escolha <=0 or escolha >= 3:
            print("Opção inválida. Por favor, tente novamente.")

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