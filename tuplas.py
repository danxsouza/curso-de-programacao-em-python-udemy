"""
tuplas (tuple)
Tuplas são bastente parecidas com listas.
Existem basicamente duas diferenças básicas:

1 -  As tuplas são representadas por parênteses ()
2 - As tuplas são imutáveis: Isso significa ao se criar uma tupla ela não muda. Toda
operação em uma tupla gera uma nova tupla
"""
# Cuidado: 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6,)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6,
print(tupla2)

print(type(tupla2))

# Cuidado: 2: Tuplas com 1 elemento

tupla3 = (4) # Isso não é uma tupla, é um INT
print(tupla3)

print(type(tupla3))

tupla4 = 4,  # Isso é uma tupla
print(tupla4)
print(type(tupla4))

tupla5 = (4,)
print(tupla5)
print(type(tupla5))
# Conclusão: Podemos definir que tuplas são definidas pela virgula e não pelo uso de parênteses.

# Podemos gerar uma tupla dinâmicamente com o range(inicio, fim, passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de Tupla

tupla = ('Geek University', 'Programação em Python Essencial')

escola, curso = tupla

print(escola)
print(curso)

# OBS: Gera erro(value erro) se colocarmos um número diferente de elementos para desempacotar.

# Métodos para adição e remoção de elementos nas tuplas, não existem, dado o fato das tuplas serem imutáveis.

tupla = (1, 2, 3, 5, 10, 20)
print('O valor da soma é: ', (sum(tupla)))
print('O valor máximo é: ', (max(tupla)))
print('O valor minimo é: ', (min(tupla)))
print('O tamanho da tupla é: ', (len(tupla)))

# Contatenção de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)  # Tuplas são imutáveis

print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2  # Tuplas são imutáveis, mas podemos sobescrever seus valores

# Verificar se determinado elemento esta contido na tupla

tupla = (1, 2, 3)
print(3 in tupla)

# Interando sobre uma tupla

tupla = (1, 2, 3)
for n in tupla:
    print(n)

    for indice, valor in enumerate(tupla):
        print(indice, valor)

print('-#'*40)
print('--'*40)

tupla = 'a', 'b', 'c', 'a', 'b'
print(tupla.count('a'))

# Dicas de utilização de Tuplas

# Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção.

#Exemplo 1

meses = ('janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses)

# O acesso de elementos de uma tupla tambem é semelhante a de uma lista

print(meses[4])

# Iterable com while

i = 0
while i < (len(meses)):
    print(meses[i])
    i = i + 1
print('-'*40)
# Verificamos em qual indice o elemento esta na tupla
print(meses.index('Junho'))

# Obs: Caso o elemento não exista na lista, será gerado um erro (ValueError)

# Slicing
# Tupla(inicio, fim: passo)

print(meses[2:])

# Por que utilizar Tuplas

# - Tuplas são mais rápidas que Listas.
# - Tuplas deixam seus código mais seguro. Isso porque trabalhar com elementos imutáveis traz segurança p/ código.


# - Copiando uma tupla para outra.

tupla = (1, 2, 3)
print(tupla)

nova = tupla

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra
print(nova)
print(tupla)














