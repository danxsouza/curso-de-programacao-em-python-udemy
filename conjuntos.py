"""
Conjuntos
- Conjuntos em qualquer lingaguem de programação, estamos fazendo referência à teoria dos Conjuntos da Matemática.
- Aqui no Python, os conjuntos são chamados de Sets.
- Dito isto, da mesma forma que na matemática:
- Sets(conjuntos) não possuem valores duplicados;
- Set(conjuntos) não possuem valores ordenados;
- Elementos não são acessados via indice, ou seja, conjuntos não são indexados
Conjuntos são bons para se utilizar quando precisamos armazenar elementos, mas não nos importamos com a ordenação
deles. Quando não precisamos se preocupar com chaves, valores e itens duplicados.
Os Conjuntos(sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos(Sets) e Maps(Dicionários) em Python
 - Um dicionário tem chave/valor;
 - Um conjunto tem apenas valor;
"""
# Definindo um conjunto
# Forma 1
s = set({1, 2, 3, 3, 3, 4, 5, 5, 6, 7})  # Repare que temos valores repetidos.
print(s)
print(type(s))
# Obs: Ao criar um conjunto, caso seja adicionado um valor já existente o mesmo será ignorado, sem gerar erros e não
# fará parte do conjunto

# Forma 2 = Mais Comum
s = set({1, 2, 3, 4, 5, 5})
print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

print('--'*40)
# Importante lembrar além de não termos valores dupĺicados, não temos ordem

dados = 99, 2, 34, 23, 12, 1, 44, 5

lista = [dados]
print('Lista', lista)


tupla = tuple(dados)
print('Tupla: ', tupla)


dicionario = {}.fromkeys([dados, 'dict'])
print(f'Dicionário: {dicionario}')


conjunto = set(dados)
print(f'Conjunto: {conjunto}')


# Usos interassante com sets
# Imagine que fizemos um formulários de cadastrado de visitante em uma feira ou museu e os visitantes
# informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já quem uma lista podemos adicionar novos elementos e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiába', 'Campo Grande', 'São Paulo', 'Cuiába']
print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas. Ou seja, únicas temos.

# Podemos utilizar o set para isso
print(len(set(cidades)))

# Adicionando elementos em um conjunto
s = {1, 2, 3}
s.add(4)
s.add(4)  # Duplicidade não gera erro. Simplesmente é ignorado
print(s)

# Remover dados em um conjunto
print('-'*40)
# Forma 1
s = {1, 2, 3}
print(s)
s.remove(3)  # Não é indice informamos o valor a ser removido.
print(s)
# OBS: Caso o valor não seja encontrado, será gerado o erro Key Error

# Forma 2
s.discard(2)
print(s)
# OBS: Se o valor não for encontrado nenhum erro é informado

print('-'*40)
# Copiando um conjunto para outro...
s = { 1, 2, 3}
print(s)
# Forma 1 = Deep Copy

novo = s.copy()
print(novo)

novo.add(4)
print(novo)
print(s)

print('-'*40)
# Forma 2 - Shallow Copy
novo = s
novo.add(4)
print(novo)
print(s)


# Podemos remover todos os itens de um conjunto

s.clear()
print(s)

# Métodos Matemáticos de Conjuntos
# Imagine que temos 2 conjuntos: Um contento estudantes do curso Python e um contento estudantes do curso de Java

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam Python, também estudam java
# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando Union
print('-'*40)
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - Utlizando o &

ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar um conjunto de estudantes que não estão no outro curso

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

# Forma 2 - Utilizando o caractere pipe

unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)
