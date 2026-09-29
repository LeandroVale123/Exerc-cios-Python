titulos=[]
autores=[]


titulo=input("Digite o título do livro: ")
autor=input("Digite o autor do livro: ")

def cadastrar_livro(titulo, autor):
    titulos.append(titulo)
    autores.append(autor)
    print("Livro cadastrado com sucesso!")

def livros_cadastrados():
    if len(titulos) == 0:
        print("Nenhum livro cadastrado.")
    else:
        print("\n--- LISTA DE LIVROS ---")
        for i in range(len(titulos)):
            print(f"{i+1}. Título: {titulos[i]}, Autor: {autores[i]}")

    
livros_cadastrados()





