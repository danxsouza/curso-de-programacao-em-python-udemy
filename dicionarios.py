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


# Podemos verificar se determinada chave se encontra em um dicionário
print('br' in paises)
print('ru' in paises)
print('us' in paises)

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla, dicionário, como chaves
# de dicionários.

# Tupla por exemplo são bastante interessante de serem utilizadas como chaves de dicionários, pois as mesma são
# imutáveis.
localidades = {

    (35.6895, 39.6917): 'Escritório em Tókio',
    (70.6895, 70.6917): 'Escritório em Nova York',
    (85.6895, 85.6917): 'Escritório em São Paulo'
}
print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 200, 'mar': 500}
print(receita)
print(type(receita))

# Forma 1 - Mais Comum
receita['abr'] = 600
print(receita)

# Forma 2

novo_dado = {'maio': 800}
receita.update(novo_dado)
print(receita)

# Atulizando dados em um dicionário
# Forma 1
receita['maio'] = 550
print(receita)

# Forma 2
receita.update({'maio': 1000})
print(receita)
# CONCLUSÃO 1: A forma de adicionar novos elemente ou atualizar dados num dicionário é a mesma
# CONCLUSÃO 2: Em dicionários, NÃO podeos ter chaves repetidas

# Remover dados de um dicionário

# Forma 1 - Mais Comum
print('-'*40)
receita = {'jan': 100, 'fev': 200, 'mar': 500}
print(receita)
ret = receita.pop('mar')
print(ret)
print(receita)
# OBS 1: Aqui precisamos sempre informar a chave, e caso não encontre o elemento, um Key error é retornado
# OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado.
print('-'*40)
# Forma 2
# Neste caso ele não retorna o valor após deletar
del receita['fev']
print(receita)

print('-'*50)
# Se a chave não existir será gerado um Key Error
# del receita['fev']
# print(receita)

# Imagine que você tem um comércio eletronico, onde temos um carrinho de compras na qual adicionamos protudos.
"""
Carrinho de compras:
    Produto 1:
    - Nome
    - Quantidade
    - Preço
    
    Produto 2
    - Nome
    - Quantidade
    - Preço
    
"""
# 1 -  Poderiamos utilizar uma lista para isso? Sim
carrinho = []
produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God Of War', 1, 140.00]
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
# Teriamos que saber qual é o indice de cada informação no produto.

print('-'*50)
# Forma 2 - Pderiamos utilizar uma tupla para isso? Sim
produto1 = ('Playstation 4', 1, 2300.00)
protudo2 = ('God of War 4', 1, 150.00)
carrinho = (produto1, produto2)
print(carrinho)

print('-'*40)
# Forma 3 - Poderiamos utilizar um dicionário para isso? Sim
# Desta forma adicionamos ou removemos produtos ao carrinho e em cada produto podemos ter a certeza sobre cada
# informação
carrinho = []
produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'Preço': 2300.000}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'Preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

print('-'*50)
# Métodos de dicionários.
dic = dict(a=1, b=2, c=3)
print(dic)

# Limpar o dicionário (Zerar Dados)
# dic.clear()
# print(dic)

# Copiando um dicioário para outro
# Forma 1 - Deep Coopy
novo = dic.copy()

novo['d'] = 4
print(dic)
print(novo)

print('//'*50)
# Forma 2 - Shallow Copy
novo = dic
print(novo)
novo['d'] = 4
print(dic)
print(novo)

print('//'*50)
# Forma não usual de criação de dicionários
outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

# O método FROMKESY recebe dois parâmetros: um interável e um valor
# Ele vai gerar para cada valor do interável uma chave e irá atribuir a esta chave o valor informado.
usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))


