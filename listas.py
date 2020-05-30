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


