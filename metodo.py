elif opcao == "4":
    print("\n4) Exibir quantidade de manifestações\n")

    consultaManifesto = 'select count(*) from codigo'
    codigo = listarBancoDados(conexao, consultaManifesto)
    quantidade = codigo[0][0]

    print("A quantidade total de manifestações é", quantidade, "\n")

print("-" * 54)
