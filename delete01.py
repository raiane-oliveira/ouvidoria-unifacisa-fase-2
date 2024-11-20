#Para exibir a manifestacao

def exibir_manifestacao(conexao: object, codigo: object) -> object:
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("select * from manifestacao where codigo +%s", (codigo))
    manifestacao = cursor.fetchone()
    cursor.close()

    if manifestacao:
        print("\nCódigo da Manifestação:", manifestacao["codigo"])
        print("\nConteúdo da Manifestação:", manifestacao["conteudo"])
        print("\nTipo da Manifestação:", manifestacao["tipo"])
    else:
        print("\nManifestação não foi encontrada.")
    return manifestacao

#Para confirmar a exclusão:

def confirmar_excluir():
    confirmar = ""
    while confirmar not in ["sim", "não"]:
        confirmar = input("Você deseja excluir a manifestação selecionada? (sim/não)").strip().lower()
        if confirmar not in ["sim", "não"]:
            print("Opção selecionada é inválida")
    return confirmar == "sim"

#Para excluir:

def excluir_manifestacao(conexao):
    codigoManifestacao = input("Digite o código da manifestação a ser excluída: ")
    manifestacao = exibir_manifestacao(conexao, codigoManifestacao)

    if manifestacao:
        if confirmar_excluir():
            try:
                cursor = conexao.cursor()
                cursor.execute("DELETE FROM manifestacoes WHERE codigo = %s", (codigoManifestacao,))
                conexao.commit()
                cursor.close()
                print("\nManifestação foi deletada com sucesso!")
            except Exception as e:
                print(f"Erro ao excluir a manifestação: {e}")
        else:
            print("\nExclusão não foi realizada.")
    else:
        print("\nManifestação não encontrada.")

def menu_principal():
    while True:
        print("\nMenu:")
        print("6) Excluir uma Manifestação pelo Código")
        print("0) Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 6:
            conexao = conexao_banco()
            excluir_manifestacao(conexao)
            conexao.close()
        elif opcao == 0:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

