from operacoesbd import *

# Nesse arquivo é onde vai todos os métodos

# Opção 06

def getPositiveInteger(prompt="Digite um número: "):
    while True:
        try:
            numero = int(input(prompt))
            if numero > 0:
                return numero
            print("Por favor, insira um número positivo.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro positivo.")

# exibir uma manifestação pelo código
def exibir_manifestacao(conexao, codigo):
    sql = "SELECT * FROM manifestacoes WHERE codigo = %s"
    manifestacao = listarBancoDados(conexao, sql, (codigo,))
    if manifestacao:
        manifestacao = manifestacao[0]
        print("\nCódigo:", manifestacao["codigo"])
        print("Conteúdo:", manifestacao["conteudo"])
        print("Tipo:", manifestacao["tipo"])
    else:
        print("\nManifestação não encontrada.")
    return manifestacao

# excluir uma manifestação pelo código
def excluir_manifestacao(conexao):
    codigo = getPositiveInteger("Digite o código da manifestação para ser excluída: ")
    if exibir_manifestacao(conexao, codigo):
        confirmacao = input("Deseja excluir esta manifestação? (sim/não): ").strip().lower()
        if confirmacao == "sim":
            sql = "DELETE FROM manifestacoes WHERE codigo = %s"
            linhas_afetadas = excluirBancoDados(conexao, sql, (codigo,))
            if linhas_afetadas > 0:
                print("\nManifestação excluída com sucesso!")
            else:
                print("\nErro ao excluir a manifestação.")
        else:
            print("\nExclusão cancelada.")

# menu principal
def menu_principal():
    endereco = "localhost"
    usuario = "root"
    senha = "senha"
    banco = "meu_banco"

    conexao = criarConexao(endereco, usuario, senha, banco)
    if not conexao:
        print("Não foi possível conectar ao banco de dados.")
        return

    while True:
        print("\nMenu:")
        print("1) Excluir Manifestação")
        print("0) Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            excluir_manifestacao(conexao)
        elif opcao == "0":
            print("Retornando ao menu principal...")
            break
        else:
            print("Opção inválida. Tente novamente.")

    # Encerra a conexão no final do programa
    conexao.close()

if __name__ == "__main__":
    menu_principal()