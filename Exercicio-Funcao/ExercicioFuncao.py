#def menu ():
#    print("\n--- MENU BIBLIOTECA ---")
#    print("1. Cadastrar livro")
#    print("2. Listar livros")
#    print("3. Pesquisar livro por título")
#    print("4. Excluir livro por título")
#    print("5. Sair")
#    print("6. Total de livros cadastrados")

#menu()
livros = []

def menu ():
    print("\n1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Sair")

def livro():
    print(livros)

def erro():
    print("\nOpção inválida!")


while True:
    menu()
    opc=int(input("Escolha uma das opções: "))
    if opc == 1:
        titulo=input("\nDigite o título do livro: ")
        autor=input("Digite o autor do livro: ")
        livros.append((titulo, autor))
        print("\nLivro cadastrado com sucesso!")

    elif opc == 2:
        if len(livros) == 0:
            print("Nenhum livro cadastrado.")
        else:
            print("\n--- LISTA DE LIVROS ---")
            for i, (titulo, autor) in enumerate(livros, start=1):
                print(f"{i}. Título: {titulo}, Autor: {autor}")

    elif opc == 3:
        print("Saindo do programa...")
        break  
    else:
        erro()







