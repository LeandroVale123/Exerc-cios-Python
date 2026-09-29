operacao1=int(input("Quantas operações deseja realizar: "))
produtos=[]

for i in range(operacao1):
    menu=int(input("ESCOLHA UMA OPÇÃO:\n1 - Cadastrar produto\n2 - Procurar Produto\n3 - Remover Produto\n4 - Sair\nDigite a opção desejada: "))
    if menu==1:
        operacoes=int(input("Quantos produtos deseja cadastrar: "))  
       
        for i in range(operacoes):
            produto=input("\nDigite o nome do produto: ")
            ordem=input("\nDeseja alterar a ordem do produto (s/n): ").strip().lower()
            
            if ordem=="s":
                posicao=int(input("Digite a posição desejada para o produto: "))
                posicao_idx=max(0, min(posicao-1, len(produtos)))  # Garantir que a posição esteja dentro dos limites da lista
                produtos.insert(posicao_idx, produto)
            else:
                produtos.append(produto)
    print("\nProduto cadastrado com sucesso!")
    print("Lista de produtos cadastrados: ", produtos)

    if menu==2:
        produto_procurado=input("\nDigite o nome do produto que deseja procurar: ")
        if produto_procurado in produtos:
            print("Produto encontrado!")
           
        else:
            print("Produto não encontrado!")

    if menu==3:
        produto_remover=input("Digite o nome do produto que deseja remover: ")
        if produto_remover in produtos:
            produtos.remove(produto_remover)
            print("Produto removido com sucesso!")
            print("Lista de produtos atualizada: ", produtos)
        else:
            print("Produto não encontrado!")

    if menu==4:
        print("\nSaindo do programa...")
        break

