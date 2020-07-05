"""
Conhecido em Python como dicionários
Dicionários em Python são representados por chaves {}
"""
receita = {'jan': 100, 'feve': 200, 'mar': 300}
# Interar sobre dicionários
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f' Em {chave} recebi R$ {receita[chave]}')

    print('//'*40)

    print(receita.keys())

print('-/'*40)
for chave in receita.keys():
    print(receita[chave])

print('//'*40)

#Acessando os valores
print(receita.values())
print(':/'*40)
for chave in receita:
    print(receita.values())

print(':/:'*40)
# Desempacotamento de dicionários
for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

print('-?-'*40)
# Soma*, Valor Máximo*, Valor Minimo*, Tamanho
# * Se os valores forem todos inteiros ou reais, ou seja ponto flutuante.
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))




