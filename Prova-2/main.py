# Arquivo principal que gerencia o menu geral e chama as funções dos módulos

from livros import cadastrar_livro, listar_livros, pesquisar_livro, alterar_livro, excluir_livro
from alunos import cadastrar_aluno
from emprestimos import menu_emprestimo

def main():
    livros = []
    alunos = []
    emprestimos = []

    while True:
        print("\n" + "="*30)
        print("    SISTEMA PARA BIBLIOTECA")
        print("="*30)
        print("1 - Cadastrar Livros")
        print("2 - Listar Livros")
        print("3 - Pesquisar Livros")
        print("4 - Alterar Livros")
        print("5 - Excluir Livros")
        print("6 - Cadastrar Alunos")
        print("7 - Empréstimo de Livros")
        print("8 - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_livro(livros)
        elif opcao == "2":
            listar_livros(livros)
        elif opcao == "3":
            pesquisar_livro(livros)
        elif opcao == "4":
            alterar_livro(livros)
        elif opcao == "5":
            excluir_livro(livros)
        elif opcao == "6":
            cadastrar_aluno(alunos)
        elif opcao == "7":
            # Abre o submenu do módulo de empréstimos
            menu_emprestimo(emprestimos, livros, alunos)
        elif opcao == "8":
            print("\nAcesso Encerrado!")
            break
        else:
            print("\nOpção inválida! Escolha uma opção entre 1 e 8.")

if __name__ == "__main__":
    main()