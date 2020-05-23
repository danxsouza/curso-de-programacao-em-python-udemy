"""
Estruturas Lógicas, and(e), or(ou) not(não) is(é)
Operadores unários
 - not
 Operadores binários
 - and, or, is

 Para o 'and', ambos os valores precisam ser true
 Para o 'or' um ou outro valor precisa ser True
 Para o 'not' o valor do booleano é invertido, ou seja, se for True, virá False, se for False, vira True
"""

ativo = True
logado = False

print('-'*50)
print('========função and=====================================')
if ativo and logado:
    print('Bem vindo Usuário')
else:
    print('Vocẽ precisa ativar sua conta, ative seu email')

print('-'*50)
print('=====função or ========================================')

if ativo or logado:
    print('Bem vindo Usuário')
else:
    print('Vocẽ precisa ativar sua conta, ative seu email')

print('-'*50)
print('================not====================================')
if not ativo:
    print('Por favor, verificar seu email de cadastro')
else:
    print('Bem vindo usuário')

print('-'*50)
print('===============is======================================')
print(ativo is False)