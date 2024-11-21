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
    print("4) Voltar ao menu principal")

#todo: Metodo de criação de manifestações no banco de dados
def criarManifestacao(conexao, tipo):
    autor = input("Digite seu nome: ")
    conteudo = input(f"Digite sua(eu) {tipo.lower()}: ")

    inserirManifestacao = "INSERT INTO manifestacoes (tipoManifestacao, autor, manifestacao) VALUES (%s, %s, %s)"
    valores = [tipo, autor, conteudo]

    insertNoBancoDados(conexao, inserirManifestacao, valores)
    print(f"{tipo} registrado(a) com sucesso!")

#todo: perguntar ao usuario se ele quer fazer uma nova manifestação ou voltar ao menu
    while True:
        criarManifestacaoNovamente = getPositiveInteger("\nDeseja criar uma nova manifestação?\n1) Sim\n2) Não\n")
        if criarManifestacaoNovamente == 1:
            break
        elif criarManifestacaoNovamente == 2:
            return
        else:
            print("Opção inválida!")

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
            return
        else:
            print("Opção inválida!")

def listarManifestacoes(conexao):
    consultarListagem = 'SELECT * FROM ouvidoria'
    listaManifestacao = listarBancoDados(conexao, consultarListagem)
    if len(listaManifestacao) == 0:
        print('Não há reclamações registradas')
    else:
        print()
        print('Listando reclamações...')
        for Manifestacao in listaManifestacao:
            print('Código: ', Manifestacao[0])
            print('Conteudo: ', Manifestacao[1])
            print('Tipo: ', Manifestacao[2])
            print('Autor: ', Manifestacao[3])
            print('createdAt: ', Manifestacao[4] )
            print()
def pesquisarPorCodigo(conexao):
    codigoParaPesquisa = getPositiveInteger("Insira o código da manifestação que você deseja ver?")
    pesquisarCodigo = "SELECT * FROM ouvidoria where codigo = %s"
    codigo =[codigoParaPesquisa]
    exibirManifestacaoPorcodigo = listarBancoDados(conexao, pesquisarCodigo,codigo)
    if exibirManifestacaoPorcodigo:
        for manifestacao in exibirManifestacaoPorcodigo:
            print(manifestacao[0],":",manifestacao[2],"-",manifestacao[1],
                  "/n-",manifestacao[3],"-",manifestacao[4])
    else:
        print("Não existe manifestação com esse código")