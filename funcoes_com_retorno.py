# -*- coding: UTF-8 -*-
"""
  Funções com retorno

numeros = [1, 2, 3]

retorno_pop = numeros.pop()

print(f'Retorno do pop: {retorno_pop}')

retorno_print = print(numeros)

print(f'Retorno do print: {retorno_print}')

Obs: Não precisamos necessiamente criar uma variável para receber o retorno de
uma função. Podemos passar a execução da funçao para outra função.

def quadrado_de_7():
    return 'Oi'

print(quadrado_de_7())

alguem = "Pedro"
print(quadrado_de_7() + alguem)


# OBS: Sobre a palavra return
# 1 - Ela finaliza a função, ou seja, ela sai da execução da função.
# 2 - Podemos ter em uma função, diferente return;
# 3 - Podemos em uma função, retornar qualquer tipo de dado e até mesmo, multiplos valores;

# Exemplo 1

def diz_oi():
    return 'Oi'
    print('Estou sendo executado apos o retorno....')

print(diz_oi())


# Exemplo 2

def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    else:
        return 'b'

print(nova_funcao())


# Exempo 3
def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)



# Vamos criar uma função para jogar a moeda
# Gera um número pseudo-randômico entre zero e um.

from random import random


def joga_moeda():


    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())

"""

# Erros comuns na utilização do retorno, que na verdade nem é erro, mas sim codificação desnecessária.


def eh_impar():
    numero = 4
    if numero % 2 != 0:
        return True
    return False
print(eh_impar())
