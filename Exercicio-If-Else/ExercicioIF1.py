nome=input("Nome do Usuario?: ")
problema1=input("Problema 1: Indisponibilidade total do sistema (s/n)?: ").strip().lower()
if problema1 == "s":
    prob_es="Indisponibilidade total do sistema"
    prioridade="Critica"
else:
    problema2=input("Problema 2: Sistema funcionando, mas com lentidão ou erros (s/n)?: ").strip().lower()
    if problema2 == "s":
        prob_es="Sistema funcionando, mas com lentidão ou erros"
        prioridade="Alta"
    else:
        problema3=input("Problema 3: Problema impede o trabalho (s/n)?: ").strip().lower()
        if problema3 == "s":
            prob_es="Problema impede o trabalho"
            prioridade="Média"
        else:
            problema4=input("Problema 4: Outros problemas (s/n)?: ").strip().lower()
            if problema4 == "s":
                prob_es="Outros problemas"
                prioridade="Baixa"
            else:
                prob_es="Erro no registro"
                prioridade="N/A"
tempo=input("A quanto tempo o problema vem ocorrendo?: ")

print(f"Nome do Usuario: {nome}")
print(f"Tempo de duração do problema: {tempo}")
print(f"Descrição do problema: {prob_es}")
print(f"Prioridade: {prioridade}")