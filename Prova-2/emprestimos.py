# emprestimos.py
# Módulo responsável pelo gerenciamento dos empréstimos e devoluções

from datetime import date, timedelta

def realizar_emprestimo(emprestimos, livros, alunos):
    print("\n--- REALIZAR EMPRÉSTIMO ---")
    
    matricula_aluno = input("Matrícula do aluno: ").strip()
    if matricula_aluno == "":
        print("Erro: Matrícula do aluno é obrigatória!")
        return

    # Busca o aluno na lista
    aluno_selecionado = next((a for a in alunos if a["matricula"] == matricula_aluno), None)
    if aluno_selecionado is None:
        print("Erro: Aluno não cadastrado no sistema! Cadastre-o primeiro.")
        return

    # Verifica se o aluno está suspenso por ter devolvido com atraso
    hoje = date.today()
    if aluno_selecionado.get("bloqueado_ate") and hoje < aluno_selecionado["bloqueado_ate"]:
        dias_restantes = (aluno_selecionado["bloqueado_ate"] - hoje).days
        print(f"Erro: O aluno está impossibilitado de realizar novos empréstimos por mais {dias_restantes} dia(s).")
        return

    codigo_livro = input("Código do livro: ").strip()
    if codigo_livro == "":
        print("Erro: Código do livro é obrigatório!")
        return

    # Busca o livro na lista
    livro_selecionado = next((l for l in livros if l["codigo"] == codigo_livro), None)
    if livro_selecionado is None:
        print("Erro: Livro não encontrado no sistema! Cadastre-o primeiro.")
        return

    # Verifica se há estoque disponível
    if livro_selecionado["quantidade"] <= 0:
        print("Não é possível realizar o empréstimo. Não há exemplares disponíveis.")
        return

    # Atualiza o estoque do livro
    livro_selecionado["quantidade"] -= 1

    # Define a data do empréstimo e o prazo de entrega de 7 dias
    data_emprestimo = hoje
    data_entrega = data_emprestimo + timedelta(days=7)

    # Registro do empréstimo
    novo_emprestimo = {
        "codigo_livro": livro_selecionado["codigo"],
        "titulo_livro": livro_selecionado["titulo"],
        "matricula_aluno": aluno_selecionado["matricula"],
        "nome_aluno": aluno_selecionado["nome"],
        "data_emprestimo": data_emprestimo,
        "data_entrega": data_entrega,
        "status": "Ativo"
    }
    emprestimos.append(novo_emprestimo)

    print(f"\nEmpréstimo do livro '{livro_selecionado['titulo']}' para o(a) aluno(a) '{aluno_selecionado['nome']}' realizado com sucesso!")
    print(f"Data do empréstimo: {data_emprestimo.strftime('%d/%m/%Y')}")
    print(f"Data limite para entrega (7 dias): {data_entrega.strftime('%d/%m/%Y')}")
    print(f"Restam {livro_selecionado['quantidade']} exemplar(es) deste livro no estoque.")


def listar_emprestimos(emprestimos):
    print("\n--- EMPRÉSTIMOS REALIZADOS ---")
    emprestimos_ativos = [e for e in emprestimos if e["status"] == "Ativo"]

    if not emprestimos_ativos:
        print("Nenhum empréstimo ativo registrado no momento.")
        return

    hoje = date.today()

    for e in emprestimos_ativos:
        # Condição para status de atraso ou em dia
        if hoje > e["data_entrega"]:
            status = "ATRASADO"
        else:
            status = "Em dia"

        print(f"\nLivro: {e['titulo_livro']} (Código: {e['codigo_livro']})")
        print(f"Aluno: {e['nome_aluno']} (Matrícula: {e['matricula_aluno']})")
        print(f"Data do Empréstimo: {e['data_emprestimo'].strftime('%d/%m/%Y')}")
        print(f"Data Prevista de Entrega: {e['data_entrega'].strftime('%d/%m/%Y')}")
        print(f"Status: {status}")


def devolver_livro(emprestimos, livros, alunos):
    print("\n--- DEVOLVER LIVRO ---")
    matricula = input("Matrícula do aluno: ").strip()
    codigo_livro = input("Código do livro devolvido: ").strip()

    # Procura o empréstimo ativo correspondente
    emprestimo_encontrado = None
    for e in emprestimos:
        if e["matricula_aluno"] == matricula and e["codigo_livro"] == codigo_livro and e["status"] == "Ativo":
            emprestimo_encontrado = e
            break

    if emprestimo_encontrado is None:
        print("Erro: Nenhum empréstimo ativo encontrado para essa matrícula e livro!")
        return

    hoje = date.today()
    emprestimo_encontrado["status"] = "Devolvido"

    # Restitui a quantidade do livro ao estoque
    livro = next((l for l in livros if l["codigo"] == codigo_livro), None)
    if livro:
        livro["quantidade"] += 1

    # Verifica se passou dos 7 dias
    if hoje > emprestimo_encontrado["data_entrega"]:
        dias_atraso = (hoje - emprestimo_encontrado["data_entrega"]).days
        aluno = next((a for a in alunos if a["matricula"] == matricula), None)
        
        if aluno:
            # Bloqueia por 14 dias a partir da data atual
            aluno["bloqueado_ate"] = hoje + timedelta(days=14)
            print(f"\nAtenção: Livro devolvido com {dias_atraso} dia(s) de atraso!")
            print("O aluno foi penalizado e NÃO poderá realizar novos empréstimos por 14 dias.")
    else:
        print("\nDevolução realizada com sucesso dentro do prazo!")


def menu_emprestimo(emprestimos, livros, alunos):
    # Submenu exclusivo para a gestão de empréstimos
    while True:
        print("\n" + "-"*30)
        print("    SUBMENU - EMPRÉSTIMOS")
        print("-"*30)
        print("1 - Realizar Empréstimo")
        print("2 - Empréstimos Realizados")
        print("3 - Devolver Livro")
        print("4 - Voltar para o Menu Principal")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            realizar_emprestimo(emprestimos, livros, alunos)
        elif opcao == "2":
            listar_emprestimos(emprestimos)
        elif opcao == "3":
            devolver_livro(emprestimos, livros, alunos)
        elif opcao == "4":
            print("Retornando ao menu principal...")
            break
        else:
            print("Opção inválida! Escolha uma opção entre 1 e 4.")