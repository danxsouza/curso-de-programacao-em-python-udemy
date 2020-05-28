"""
Saindo de Loops com break
- Funciona da mesma forma que nas linguagens C ou Java.
Utilizamos para sair de loops de maneira forçada ou de maneira projetada.
"""

# Exemplo 1
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print("Saio do Loop")

# Exemplo 2

while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == 'sair':
        break
