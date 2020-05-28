"""
- Precisamos entender o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loop for.

Ranges são utilizados para gerar sequências númericas. Não de forma aleatória, mas sim de maneira especificada.

Forma gerais:
range(valor_de_parada)

OBS: valor_de_parada não inclusive (inicio padrão 0 e passo de 1 em 1)
"""
# Forma 1

for num in range(11):
    print(num)

print('-'*40)

# Forma 2
# range(valor_de_inicio, valor_de_parada)

for num in range(1, 11):
    print(num)

print('-'*40)

# Forma 3 - Passo de 2 em 2
# range(valor_de_inicio, valor_de_parada, passo)
for numero in range(5, 50, 5):
    print(numero)

print('-'*40)

# Forma 4
# range(valor_inicio, valor_de_parada, passo) - Valor descrecente(inverso)
for numero in range(10, 0, -1):
    print(numero)
