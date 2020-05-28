"""
loop while
Forma Geral
while espressão_booleana:
  //execução

- O blodo do while será repetido enquanto a expressão booleana for verdadeira.

Expressão Boolean é toda expressão onde o resultado é verdadeiro ou valso.

- Exemplos:
num = 5
num < 5
"""

numero = 1
while numero < 10:
    print(numero)
    numero += 1

# OBS: Em um Loop While, é importante que cuidemos do critério de parada para não criar um loop infinito


# Exemplo 2
resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou?')


