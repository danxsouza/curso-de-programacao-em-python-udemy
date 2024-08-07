#-*- coding: UTF-8 -*-
"""
Módulo Collections - Deque
Podemos dizer que o deque é uma lista de alta performace
"""
# importar

from collections import deque

# Criando deques

deq = deque('Geek')

print(deq)

# Adicionando elementos no deque

deq.append('y')  # adiciona no final
print(deq)

deq.appendleft('k')  # Adiciona no começo da lista
print(deq)

# Remover elementos

print(deq.pop())  # Remove e retornar o último elemento

print(deq)

print(deq.popleft())  # Remove e retorna o primeiro elemento

print(deq)