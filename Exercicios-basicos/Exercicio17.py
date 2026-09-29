n1=int(input("Digite um número: "))
n2=int(input("Digite outro número: "))
divisao=n1/n2
resto=n1%n2
if resto == 0:
    print(f"O número é divisível e o seu resultado é: {divisao}")
else:
    print(f"O número não é divisível inteiro e o seu resto é : {resto}")
    

