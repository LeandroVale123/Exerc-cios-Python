# alunos.py
# Módulo responsável pelo gerenciamento de alunos

def cadastrar_aluno(alunos):
    qtd_alunos_in = input("\nQuantos alunos deseja cadastrar? ").strip()

    if qtd_alunos_in == "" or not qtd_alunos_in.isdigit():
        print("Erro: Quantidade inválida ou em branco!")
        return

    qtd_alunos = int(qtd_alunos_in)
    for i in range(1, qtd_alunos + 1):
        print(f"\n--- ALUNO {i} ---")
        matricula = input("Matrícula: ").strip()

        if matricula == "":
            print("Erro: A matrícula deve ser informada corretamente!")
            break

        # Verifica duplicidade de matrícula
        matricula_existente = any(a["matricula"] == matricula for a in alunos)
        if matricula_existente:
            print("Erro: Já existe um aluno cadastrado com esta matrícula!")
            break

        nome = input("Nome: ").strip()
        if nome == "":
            print("Erro: O nome do aluno não pode ser deixado em branco!")
            break

        turma = input("Turma: ").strip()
        if turma == "":
            print("Erro: A turma não pode ser deixada em branco!")
            break

        aluno_novo = {
            "matricula": matricula,
            "nome": nome,
            "turma": turma,
            "bloqueado_ate": None  # Armazena a data limite de bloqueio caso entregue com atraso
        }
        alunos.append(aluno_novo)
        print("Aluno cadastrado com sucesso!")