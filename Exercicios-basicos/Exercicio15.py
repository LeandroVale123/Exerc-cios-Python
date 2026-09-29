salario=float(input("Digite o valor do seu salário: "))
percentual=float(input("Digite o percentual de aumento: "))
aumento=salario*(percentual/100)
novo_salario=salario+aumento
print("O aumento foi de R$: ", aumento)
print("O novo salário é de R$: ", novo_salario)