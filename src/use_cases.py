from operacoesbd import *
from src.helpers import getPositiveInteger


# Nesse arquivo é onde vai todos os métodos

#todo: OPÇÃO 3) CRIAR MANIFESTAÇÕES
# Menu de opções de manifestações
def menuManifestacoes():
    print("\nEscolha o tipo de manifestação")
    print("1) Reclamação")
    print("2) Sugestão")
    print("3) Elogio")
    print("4) Sair")

#todo: Metodo de criação de manifestações no banco de dados
def criarManifestacao(conexao, tipo):
    autor = getPositiveInteger("Digite seu nome: ")
    conteudo = getPositiveInteger(f"Digite sua {tipo.lower()}: ") #CRIAR CORREÇÃO PARA O GÊNERO

    inserirManifestacao = "insert into manifestacoes (tipoManifestacao, autor, manifestacao) VALUES (%s, %s, %s)"
    valores = [tipo, autor, conteudo]

    insertNoBancoDados(conexao, inserirManifestacao, valores)
    print(f"{tipo} registrada com sucesso!")

#todo: execução do menu
def executarMenuCriar(conexao):
    opcao = -1
    while opcao != 4:
        menuManifestacoes()
        opcao = getPositiveInteger("\nDigite a opção desejada: ")

        if opcao == 1:
            print("\nRegistro de Reclamação")
            criarManifestacao(conexao, "Reclamação")
        elif opcao == 2:
            print("\nRegistro de Sugestão")
            criarManifestacao(conexao, "Sugestão")
        elif opcao == 3:
            print("\nRegistro de Elogio")
            criarManifestacao(conexao, "Elogio")
        elif opcao == 4:
            print("Obrigado pela preferência!\nVolte sempre!")
        else:
            print("Opção inválida!")