#-*- coding: UTF-8 -*-
"""
Definindo funções

- Funções são pequenas partes de código que realizam tarefas especificas;
- Pode ou não receber entradas de dados e retornar uma saida de dados;
- Muito úteis para executar procedimentos similiares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela;
é bom fazer uma verificação para que a função seja simplificada

Já utilizamos várias funções desde que iniciamos este curso.
Exemplos:
-print()
-len()
-max()
-count()
"""
# Exemplo de utilização de funções:

#cores = ['verde', 'amarela', 'azul', 'branca']

# Utilizando uma função integrada do Python (Built-in do Python)
# print(cores)

# cores.append('roxo')
# print(cores)

# print(help(print))

# Como definir funções.
"""
  Em Python, a forma geral de definir uma função

  def nome_da_funcao(paramêtro_de_entrada):
    bloco_da_funcao

    Onde:

    nome_da_funcao - SEMPRE com letra minúsculas, e se for nome composto, separado por underline(Snake Case);
    parmetros de entrada -> Opcionais, onde tendo mais de um, cada um separado por ponto e virgual, pode ser opcional
    ou não.
    
    Bloco da função -> Também chamado corpo da função ou implementação é onde o processamento da função acontece, neste
    bloco pode ter ou não, retorno da função.

    OBS: Para definir uma função, utilizamos a palavra reservada, "def" informando ao python que estamos definindo uma
    função. Também abrimos o  bloco de código com o já conhecido dois pontos : que é definido utilizando em Python 
  """

# Definindo a primeira função


def diz_oi():
    print('Oi')


"""
    OBS: 
    1 - Veja que dentro das nossa funções, podemos utilizar outras funções;
    2 - veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer "oi"
    3 - Veja que esta função, não recebe nenhum parâmetro de entrada.
    4 - Veja que esta função não retorna nada.

"""
# utilizando a função

diz_oi()

# Exemplo 2


def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante')


cantar_parabens()

#for n in range(5):
#    print(n)
#    cantar_parabens()

# Em python, podemos inclusive criar variavel do tipo de uma função e executar essa função através da variavel

canta = cantar_parabens
canta()