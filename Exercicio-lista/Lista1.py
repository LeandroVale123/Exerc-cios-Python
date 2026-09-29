nomes=["Ana", "Carlos", "João", "Leandro", "Kalel"]
idade=[18, 22, 19, 35, 2]

print(nomes[0], idade[0]) #Ana 18
print(nomes [-1], idade[-1]) #Kalel 2

print(len(nomes)) #para identificar o tamanho da lista
print(nomes) #mostra todos os nomes da lista

nomes.append("Maria") #adiciona um nome no final da lista
print(nomes) #mostra todos os nomes da lista

nomes.insert(2, "Pedro") #adiciona um nome em uma posição específica da lista
print(nomes) #mostra todos os nomes da lista

nomes.remove("João") #remove um nome da lista
nomes.pop(0) #remove o primeiro nome da lista
print(nomes) #mostra todos os nomes da lista

#lista.append(valor) - acrescenta um elemento no final da lista
#lista.insert(posição, valor) - acrescenta um elemento em uma posição específica da lista
#lista.remove(valor) - remove um elemento da lista
#lista.pop(posição) - remove um elemento de uma posição específica da lista 
#len(lista) - retorna o tamanho da lista

# 4. LISTAS E O LAÇO FOR

nomes=['Carlos', 'Pedro', 'Leandro', 'Kalel', 'Maria']

for nome in nomes:
    print(nome) #mostra todos os nomes da lista 

idades=[18, 22, 19, 35, 2]

for idade in idades:
    print(idade) #mostra todas as idades da lista

notas=[7.5, 8.0, 9.5, 6.0, 10.0, 7.5] #soma das notas é 41.0
soma=0

for nota in notas:
    soma+=nota #soma todas as notas da lista
    print(soma) #mostra a soma das notas da lista

for indice, nome in enumerate(nomes):
    print(indice, nome) #mostra o índice e o nome da lista

# 5. Outras Operações com listas

print(max(notas)) #mostra a maior nota da lista
print(min(notas)) #mostra a menor nota da lista
print(sum(notas)) #mostra a soma das notas da lista
print(sum(notas)/len(notas)) #mostra a média das notas da lista

nomes.sort() #ordena a lista em ordem alfabética
print(nomes) #mostra todos os nomes da lista ordenada

nomes.sort(reverse=True) #ordena a lista em ordem alfabética reversa
print(nomes) #mostra todos os nomes da lista ordenada reversa

nome="Leandro"
if nome in nomes:
    print("Nome encontrado!")
else:
    print("Nome não encontrado!")

print(notas.count(7.5)) #conta quantas vezes o valor 7.5 aparece na lista  
nova=nomes.copy() #cria uma cópia da lista nomes
