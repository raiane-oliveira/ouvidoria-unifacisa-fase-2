from use_cases import *
from helpers import goBackToMenu

conexao = criarConexao("localhost", "root", "unifacisa", "ouvidoria")

def main():
    opcao = ""

    while opcao != "7":
        print("Seja bem-vindo ao sistema de ouvidoria da Unifacisa!\n")
        print("1) Listagem das Manifestações")
        print("2) Listagem de Manifestações por Tipo")
        print("3) Criar uma nova manifestação")
        print("4) Exibir quantidade de manifestações")
        print("5) Pesquisar uma manifestação por código")
        print("6) Excluir uma manifestação por código")
        print("7) Sair do sistema\n")

        opcao = input("Digite a sua opção: ")

        if opcao == "1":
            print("\n1) Listagem das Manifestações")
            listarManifestacoes(conexao)

            print("-" * 54)
            opcao = goBackToMenu()
        elif opcao == "2":
            print("\n2) Listagem das Manifestações por Tipo\n")
            listandoManifestacoesPorTipo(conexao)

            print("-" * 54)
            opcao = goBackToMenu()
        elif opcao == "3":
            print("\n3) Criar uma nova manifestação")
            executarMenuCriar(conexao)

            print("-" * 54)
        elif opcao == "4":
            print("\n4) Exibir quantidade de manifestações\n")

            consultaManifesto = 'select count(*) from manifestacoes'
            codigo = listarBancoDados(conexao, consultaManifesto)
            quantidade = codigo[0][0]

            print("A quantidade total de manifestações é", quantidade, "\n")

            print("-" * 54)
            opcao = goBackToMenu()
        elif opcao == "5":
            print("\n5) Pesquisar uma manifestação por código\n")
            pesquisarPorCodigo(conexao)

            print("-" * 54)
            opcao = goBackToMenu()
        elif opcao == "6":
            print("\n6) Excluir uma Manifestação pelo Código\n")
            excluir_manifestacao(conexao)

            print("-" * 54)
            opcao = goBackToMenu()
        elif opcao != "7":
            print("Opção inválida\n")

    print("\nObrigado por utilizar o programa! Volte sempre!")

try:
    main()
except KeyboardInterrupt:
    print("\nObrigado por utilizar o programa! Volte sempre!")

encerrarConexao(conexao)
