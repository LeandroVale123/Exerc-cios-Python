operacao = int(input("Quantas operações deseja realizar: "))
estoque_livros = {}

for operacao_atual in range(operacao):
 
    print("\nSISTEMA PARA BIBLIOTECA")
    
    print("\n1 - Cadastrar Livros")
    print("2 - Cadastrar Alunos")
    print("3 - Realizar Empréstimo")
    print("4 - Sair")

    opcao = input("\nEscolha uma opção: ").strip()
    
    if opcao == "1":
        qtd_livros_in = input("\nQuantos livros deseja cadastrar? ").strip()

        if qtd_livros_in == "":
            print("Erro: A quantidade de livros não pode ser deixada em branco!")
            break
        else:
            qtd_livros = int(qtd_livros_in)
            for i in range(1, qtd_livros + 1):
                print(f"\n--- LIVRO {i} ---")
                codigo = input("Código: ").strip()

                if codigo == "":
                    print("Erro: O código do livro não pode ser deixado em branco!")
                    erro = True
                else:
                    titulo = input("Título: ").strip()
                    if titulo == "":
                        print("Erro: O título não pode ser deixado em branco!")
                        erro = True
                    else:
                        autor = input("Autor: ").strip()
                        if autor == "":
                            print("Erro: O autor não pode ser deixado em branco!")
                            erro = True
                        else:
                            ano_input = input("Ano: ").strip()
                            if ano_input == "" or int(ano_input) <= 0:
                                print("Erro: O ano informado deve ser válido!")
                                erro = True
                            else:
                                quantidade_in = input("Quantidade: ").strip()
                                if quantidade_in == "" or int(quantidade_in) <= 0:
                                    print("Erro: A quantidade disponível deve ser maior que zero!")
                                    erro = True
                                else:
                                    erro = False
                                    # Salvamos o código do livro e sua quantidade no dicionário
                                    estoque_livros[codigo] = int(quantidade_in)
                                    print("Livro cadastrado com sucesso!")

                if erro:
                    break

            if erro:
                break
    
    elif opcao == "2":
        qtd_alunos_in = input("\nQuantos alunos deseja cadastrar? ").strip()

        if qtd_alunos_in == "":
            print("Erro: A quantidade de alunos não pode ser deixada em branco!")
            break
        else:
            qtd_alunos = int(qtd_alunos_in)
            for i in range(1, qtd_alunos + 1):
                print(f"\n--- ALUNO {i} ---")
                matricula = input("Matrícula: ").strip()

                if matricula == "":
                    print("Erro: A matrícula deve ser informada corretamente!")
                    erro = True
                else:
                    nome = input("Nome: ").strip()
                    if nome == "":
                        print("Erro: O nome do aluno não pode ser deixado em branco!")
                        erro = True
                    else:
                        turma = input("Turma: ").strip()
                        if turma == "":
                            print("Erro: A turma não pode ser deixada em branco!")
                            erro = True
                        else:
                            erro = False
                            print("Aluno cadastrado com sucesso!")

                if erro:
                    break

            if erro:
                break
    
    elif opcao == "3":
        print("\n--- EMPRÉSTIMO ---")
        codigo_livro = input("Código do livro: ").strip()
        if codigo_livro == "":
            print("Erro: Código do livro é obrigatório!")
            break
        if codigo_livro not in estoque_livros:
            print("Erro: Livro não encontrado no sistema! Cadastre-o primeiro.")
        else:
            matricula_aluno = input("Matrícula do aluno: ").strip()
            if matricula_aluno == "":
                print("Erro: Matrícula do aluno é obrigatória!")
                break
            else:
                qtd_disponivel = estoque_livros[codigo_livro]
                if qtd_disponivel > 0:
                    estoque_livros[codigo_livro] -= 1
                    print("Empréstimo realizado com sucesso!")
                    print(f"Restam {estoque_livros[codigo_livro]} deste livro no estoque.")
                else:
                    print("Não é possível realizar o empréstimo.")
                    print("Não há exemplares disponíveis.")
    
    elif opcao == "4":
        print("\nAcesso Encerrado!")
        break
    
    else:
        print("\nOpção inválida! escolha uma opção entre 1 e 4.")