idade=int(input("Digite a sua idade: "))
resposta=input("Você possui CURSO TECNICO? (sim/não): ").strip().lower()
cur_tec=resposta == "sim"

if idade >= 18: 
    if cur_tec:
        print("Você tem idade para trabalhar e possui curso tecnico")
    else:
        print("Você tem idade para trabalhar, mas não possui curso tecnico")
else:
    if cur_tec:
        print("Você não tem idade para trabalhar, mas possui curso tecnico")
    else:
        print("Você não tem idade para trabalhar e não possui curso tecnico")
