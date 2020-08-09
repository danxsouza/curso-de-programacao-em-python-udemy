"""
Módulo Collection - Counter(Contador)
Collections -> High-Perfomance Cotainer Datetype

Counter -> Recebe um interável com parâmetro e cria um objeto do tipo Collection Counter que é parecido
com um dicionário, contento como chave o elemento da lista passada como porâmetro e como valor a quantidade
de ocorrência desse elemento.
"""

# Utilizando o Counter

# Realizando o import
from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer interável, aqui usamos uma lista
lista = [1, 1, 2, 2, 2, 2, 1, 1, 1,1, 2, 2, 2, 4, 4, 4, 4, 4, 5, 5, 5, 5, 88, 66, 77, 43]

# Utilizando o Counter
res = Counter(lista)
print(type(res))

print(res)
# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências.

print('-'*40)

# Exemplo 2
print(Counter('Geek University'))

print('-'*40)
# Exemplo 3

texto = """ Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of 
type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into e
lectronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset 
sheets containing Lorem Ipsum passages,and more recently with desktop publishing software like Aldus PageMaker 
including versions of Lorem Ipsum. """


palavras = texto.split()
# print(palavras)
res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrências no texto
print(res.most_common(5))

