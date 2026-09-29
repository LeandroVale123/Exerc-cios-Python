# livros.py
# Módulo responsável pelo gerenciamento de livros (CRUD)

def cadastrar_livro(livros):
    qtd_livros_in = input("\nQuantos livros deseja cadastrar? ").strip()

    if qtd_livros_in == "" or not qtd_livros_in.isdigit():
        print("Erro: Quantidade inválida ou em branco!")
        return

    qtd_livros = int(qtd_livros_in)
    for i in range(1, qtd_livros + 1):
        print(f"\n--- LIVRO {i} ---")
        codigo = input("Código: ").strip()

        if codigo == "":
            print("Erro: O código do livro não pode ser deixado em branco!")
            break

        # Verifica se o código já está cadastrado na lista
        codigo_existente = any(l["codigo"] == codigo for l in livros)
        if codigo_existente:
            print("Erro: Já existe um livro cadastrado com este código!")
            break

        titulo = input("Título: ").strip()
        if titulo == "":
            print("Erro: O título não pode ser deixado em branco!")
            break

        autor = input("Autor: ").strip()
        if autor == "":
            print("Erro: O autor não pode ser deixado em branco!")
            break

        ano_input = input("Ano: ").strip()
        if ano_input == "" or not ano_input.isdigit() or int(ano_input) <= 0:
            print("Erro: O ano informado deve ser válido!")
            break

        quantidade_in = input("Quantidade: ").strip()
        if quantidade_in == "" or not quantidade_in.isdigit() or int(quantidade_in) <= 0:
            print("Erro: A quantidade disponível deve ser maior que zero!")
            break

        livro_novo = {
            "codigo": codigo,
            "titulo": titulo,
            "autor": autor,
            "ano": int(ano_input),
            "quantidade": int(quantidade_in)
        }
        livros.append(livro_novo)
        print("Livro cadastrado com sucesso!")


def listar_livros(livros):
    print("\n--- LISTA DE LIVROS ---")
    if len(livros) == 0:
        print("Nenhum livro cadastrado até o momento.")
    else:
        for l in livros:
            print(f"Código: {l['codigo']} | Título: {l['titulo']} | Autor: {l['autor']} | Ano: {l['ano']} | Qtd: {l['quantidade']}")


def pesquisar_livro(livros):
    print("\n--- PESQUISAR LIVRO ---")
    termo = input("Digite o código ou título do livro: ").strip().lower()

    if termo == "":
        print("Erro: O termo de pesquisa é obrigatório!")
    else:
        encontrados = [l for l in livros if termo == l["codigo"].lower() or termo in l["titulo"].lower()]

        if len(encontrados) > 0:
            print("\nLivro(s) encontrado(s):")
            for l in encontrados:
                print(f"Código: {l['codigo']} | Título: {l['titulo']} | Autor: {l['autor']} | Qtd: {l['quantidade']}")
        else:
            print("Nenhum livro foi encontrado com esse termo.")


def alterar_livro(livros):
    print("\n--- ALTERAR LIVRO ---")
    codigo = input("Digite o código do livro que deseja alterar: ").strip()

    livro_encontrado = next((l for l in livros if l["codigo"] == codigo), None)

    if livro_encontrado is None:
        print("Erro: Livro não encontrado no sistema!")
    else:
        print(f"Alterando dados do livro: {livro_encontrado['titulo']}")
        novo_titulo = input("Novo Título (deixe em branco para manter o atual): ").strip()
        novo_autor = input("Novo Autor (deixe em branco para manter o atual): ").strip()
        nova_qtd = input("Nova Quantidade (deixe em branco para manter a atual): ").strip()

        if novo_titulo != "":
            livro_encontrado["titulo"] = novo_titulo
        if novo_autor != "":
            livro_encontrado["autor"] = novo_autor
        if nova_qtd != "":
            if nova_qtd.isdigit() and int(nova_qtd) >= 0:
                livro_encontrado["quantidade"] = int(nova_qtd)
            else:
                print("Aviso: Quantidade inválida fornecida. Quantidade não alterada.")

        print("Cadastro do livro atualizado com sucesso!")


def excluir_livro(livros):
    print("\n--- EXCLUIR LIVRO ---")
    codigo = input("Digite o código do livro que deseja excluir: ").strip()

    livro_remover = next((l for l in livros if l["codigo"] == codigo), None)

    if livro_remover is None:
        print("Erro: Livro não encontrado no sistema!")
    else:
        livros.remove(livro_remover)
        print(f"Livro '{livro_remover['titulo']}' removido com sucesso!")