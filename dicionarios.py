"""
Dicionários

OBS: Em, algumas linguagem de programação os dicionários Python são conhecidos por mapas.
Dicionários são coleções  do tipo chave/valor.

Dicionários são representados por chaves {}.

Obs: Sobre os dicionários
 - Chave e valor são separados por dois pontos 'chave:valor';
 - Tanto chave quanto valor podem ser de qualquer tipo de dado;
 - Podemos misturar tipos de dados;
"""
print(type({}))

# Criação de dicionários

# Forma 1(Mais comum)
paises = {'br': 'Brasil', 'us': 'USA', 'ue': 'Europa'}
print(paises)
print(type(paises))

print('-'*40)
# Forma 2(Menos comum)
paises = dict(br='Brasil', us='Estados Unidos', ue='Europa')
print(paises)
print(type(paises))

print('-'*40)
# Acessando elementos
# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['us'])
print('-'*40)
# Forma 2 - Acessando via get - Recomendado
print(paises.get('br'))
print(paises.get('us'))
print(paises.get('ru'))
print('-'*40)

pais = paises.get('us', 'Não encontrado')
if pais:
    print(f'Encontrei o pais {pais}')
else:
    print('Não encontrei o pais')



