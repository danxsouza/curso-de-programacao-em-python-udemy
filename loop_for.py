"""
Loop for

Loop -> Estrutura de repetição
For -> É uma destas estruturas

C ou Java

for(int = 0; i < 10; i++){
//execução do loop
}

# Python

for item in interavel:
//execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis
Exemplo de Iteráveis
- String
    nome = 'Geek University'
- Lista
    lista = {1, 3, 5, 7}
- Range
    numeros = range(1, 10)
"""
nome = 'Geek University'
lista = {1, 3, 5, 7, 9}
numeros = range(1, 10)  # Temos que tranformar em uma lista.

# Exemplo de for 1 (Testando uma string)
for letra in nome:
    print(letra)

print('-//'*40)

# Exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)

print('-#'*40)

# Exemplod de for 3 (Iterando sobre um range)
"""
range(valor inicial, valor final)
obs: O valor final não é inclusive.
"""
for numero in range(1, 10):
    print(numero)

print('-/'*40)

"""
Enumerate:
((0, 'G'), (1 'e'), (2 'e'),(3, k'), (4, ''), (5, 'U')...)
 
"""
for indice, letra in enumerate(nome):
    print(nome[indice])

print('-'*40)
qtd = int(input('Qtas vezes você quer rodar?'))

for n in range(1, qtd+1):
    print(f'Imprimindo {n}')

print('-'*40)

nome = 'Geek University'
for letra in nome:
    print(letra, end='')

# Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
# original: U+1F603
# modificado: U0001F603


for _ in range(3):
    for numero in range(0, 11):
      print('\U0001F621' * numero)