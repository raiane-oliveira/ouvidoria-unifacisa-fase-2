from operacoesbd import *
from helpers import getPositiveInteger, formatDate


# exibir uma manifestação pelo código
def exibir_manifestacao(conexao, codigo):
    sql = "SELECT * FROM manifestacoes WHERE codigo = %s"
    manifestacao = listarBancoDados(conexao, sql, (codigo,))
    if manifestacao:
        manifestacao = manifestacao[0]
        print("\nCódigo:", manifestacao[0])
        print("Conteúdo:", manifestacao[1])
        print("Tipo:", manifestacao[2])
        print("Autor:", manifestacao[3])
        print("Criado em:", formatDate(manifestacao[4]))
    else:
        print("\nManifestação não encontrada.")
    return manifestacao


# excluir uma manifestação pelo código
def excluir_manifestacao(conexao):
    codigo = getPositiveInteger("Digite o código da manifestação para ser excluída: ")
    if exibir_manifestacao(conexao, codigo):
        confirmacao = input("\nDeseja excluir esta manifestação? (sim/não): ").strip().lower()
        if confirmacao == "sim":
            sql = "DELETE FROM manifestacoes WHERE codigo = %s"
            linhas_afetadas = excluirBancoDados(conexao, sql, (codigo,))
            if linhas_afetadas > 0:
                print("\nManifestação excluída com sucesso!")
            else:
                print("\nErro ao excluir a manifestação.")
        else:
            print("\nExclusão cancelada.")


# OPÇÃO 3) CRIAR MANIFESTAÇÕES
# Menu de opções de manifestações
def menuManifestacoes():
    print("\nEscolha o tipo de manifestação")
    print("1) Reclamação")
    print("2) Sugestão")
    print("3) Elogio")
    print("4) Voltar ao menu principal")


# Metodo de criação de manifestações no banco de dados
def criarManifestacao(conexao, tipo):
    autor = input("Digite seu nome: ")
    conteudo = input(f"Digite sua(eu) {tipo.lower()}: ")

    inserirManifestacao = "INSERT INTO manifestacao (tipo, autor, conteudo) VALUES (%s, %s, %s)"
    valores = [tipo, autor, conteudo]

    insertNoBancoDados(conexao, inserirManifestacao, valores)
    print(f"{tipo} registrado(a) com sucesso!")


# perguntar ao usuario se ele quer fazer uma nova manifestação ou voltar ao menu principal
def criarManifestacaoNovamente():
    while True:
        criarManifestacaoNovamente = getPositiveInteger("\nDeseja criar uma nova manifestação?\n1) Sim\n2) Não\n")
        if criarManifestacaoNovamente == 1:
            break
        elif criarManifestacaoNovamente == 2:
            return
        else:
            print("Opção inválida!")

# execução do menu
def executarMenuCriar(conexao):
    opcao = -1
    while opcao != 4:
        menuManifestacoes()
        opcao = getPositiveInteger("\nDigite a opção desejada: ")

        if opcao == 1:
            print("\nRegistro de Reclamação")
            criarManifestacao(conexao, "Reclamação")
            criarManifestacaoNovamente()
            return
        elif opcao == 2:
            print("\nRegistro de Sugestão")
            criarManifestacao(conexao, "Sugestão")
            criarManifestacaoNovamente()
            return
        elif opcao == 3:
            print("\nRegistro de Elogio")
            criarManifestacao(conexao, "Elogio")
            criarManifestacaoNovamente()
            return
        elif opcao == 4:
            return
        else:
            print("Opção inválida!")


def listarManifestacoes(conexao):
    consultarListagem = "SELECT * FROM manifestacoes"
    listaManifestacao = listarBancoDados(conexao, consultarListagem)
    if len(listaManifestacao) == 0:
        print("Não há manifestações registradas.")
    else:
        print()
        print("Listando manifestações...")
        for manifestacao in listaManifestacao:
            print("Código:", manifestacao[0])
            print("Conteúdo:", manifestacao[1])
            print("Tipo:", manifestacao[2])
            print("Autor:", manifestacao[3])
            print("Criado em:", formatDate(manifestacao[4]))
            print()


def pesquisarPorCodigo(conexao):
    codigoParaPesquisa = getPositiveInteger("Insira o código da manifestação que você deseja ver: ")
    pesquisarCodigo = "SELECT * FROM manifestacoes where codigo = %s"
    codigo = [codigoParaPesquisa]
    exibirManifestacaoPorcodigo = listarBancoDados(conexao, pesquisarCodigo,codigo)
    if exibirManifestacaoPorcodigo:
        for manifestacao in exibirManifestacaoPorcodigo:
            print("\nCódigo:", manifestacao[0])
            print("Conteúdo:", manifestacao[1])
            print("Tipo:", manifestacao[2])
            print("Autor:", manifestacao[3])
            print("Criado em:", formatDate(manifestacao[4]))
    else:
        print("Não existe manifestação com esse código")
