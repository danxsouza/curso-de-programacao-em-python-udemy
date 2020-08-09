"""
Módulo Collections - Default Dict


Default Dict -> Ao criar um dicionário utilizando, nós informamos um valor default, podendo utilizar um lambda para
isso. Este valor será utilizado sempre que não houver um valor definido. Caso tentamos acessar uma chave que não existe,
essa chave criada e o valor default será atribuído

OBS: Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores.
"""
# Recap Dicionários
dicionario = {'curso': 'Programação em Python: Essencial'}
print(dicionario)

print(dicionario['curso'])

# print(dicionario['outro']) # Gera um keyError

print('-'*40)
# Fazendo o import

from collections import defaultdict

dicionario = defaultdict(lambda: 0)
print(dicionario)

dicionario['curso'] = 'Programação em Python: Essencial'
print(dicionario)

print(dicionario['outro']) # KeyError no dicionário comum, mais aqui não.
print(dicionario)





