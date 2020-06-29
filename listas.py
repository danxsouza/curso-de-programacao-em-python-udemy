"""
Lista em Python funcionam como vetores/matrizes (arrays em outras linguagens) com a diferença
de serem DINÂMICO e também de podermos colocar em  QUALQUER tipo de dado.

linguagens C/Java: Arrays
 - Possuem tamanho e tipo de dado fixo.
 Ou seja, nestas linguagens se você criar um array do tipo "int" e com tamanho "5", este array
 será SEMPRE do tipo "inteiro"  e poderá ter SEMPRE no máximo "5" valores.

 Já em Python:
- Dinâmico:  Não possuem tamanho fixo: Ou seja, podemos criar a lista e sipmplesmente ir adicionando elementos.
- Qualquer tipo de dado: Não possuem tipo de dado fixo: Ou seja, podemos colocar qualquer tipo de dado
As lista em Python são representadas por colchetes: []

Lista são mutáveis, elas podem mudar constantemente.
"""

lista1 = [1, 99, 24, 4, 22, 3, 1, 42, 27, 2, 3, 70, 100, 200, 300, 340, 1]

lista2 = ['g', 'e', 'e', 'k', ' ', 'n', 'v', 'e', 'r', 's', 't', 'i']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Podemos facilmente checar se determinado valor esta contido na lista.

num = 7

if num in lista4:
    print(f'Encontrei o numero {num}')
else:
    print(f'Não encontrei o numero {num}')

# Podemos facilmente ordernar uma lista

lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrência de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

#  Adicionar Elementos em lista
"""
Para adicionar elementos em lista, utilizamos a função append
Obs: Com append, nós conseguimos adicionar um elemento por vez
"""
print(lista1)
lista1.append(42)
print(lista1)

lista1.append([8,3,1]) #Coloca a lista como elemento únic(sublista)
print(lista1)

if [8, 3, 1] in lista1: # Coloca cada elemento da lista como valor adicional a lista
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67])
print(lista1)

#  Podemos inserir um novo elemento na lista informando a posição do indice
lista1.insert(2, 'Novo valor')
print(lista1)

# Podemos facilmente juntar 2 listas
lista6 = lista1 + lista2
print(lista6)
lista1.extend(lista2)
print(lista1)

# Podemos facilmente inverter unma lista utilizando o reverse
print(80*'-')
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Copiar uma lista
lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos tem dentro da lista
print(len(lista1))

# Podemos remover facilmente o último elemento de uma lista
# OBS: O pop não somente remove o último elemento, mas tambeḿ o retorna.
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo indice
# OBS: Os elementos á direita deste indice serão deslocados para a esquerda
print(lista5)
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos(zerar a lista)

print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente converter uma string para uma lista
# Exemplo 1
curso = "Programação em Python: Essencial"
print(curso)
curso = curso.split()
print(curso)

# OBS: Por padrão o splito separa os elementos da lista pelo espaço

# Exemplo 2

curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma String
lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)
# Abaixo estamos falando: Pega a lista6 coloca espaço entre cada elemento e transforma em uma String
curso = ' '.join(lista6)
print(curso)

curso = '$'.join(lista6)
print(curso)

# Interando sobre lista

for elemento in lista2:
    print(elemento)

# Utilizando While

carrinho = []
produto = ''
while produto != 'sair':
    print("Adicionar um produto na lista ou digite 'sair' para sair")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)


