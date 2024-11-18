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

def getPositiveInteger():
    numero = -1
    while numero < 0:
        numero = int(input("Digite o número que corresponde a opção desejada"))
        if numero <= 0 or numero > 7:
            print("Número inválido. Por favor, tente novamente.")