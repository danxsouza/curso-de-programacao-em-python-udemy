"""
Escopo de Variáveis

Dois casos de escopo:

1 - Variáveis Globais;
   - Variáveis Globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.
2- Variáveis Locais;
 - Variáveis Locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo esta limitado ao bloco
 onde foi declarada.
Para declarar variáveis em Python fazemos:

nome_da_variável = valor_da_variável

Python é uma Linaguagem de tipagem dinâmica. Isso significa que ao declararmos uma váriavel, nós não colocamos o tipo
dela.
Esse tipo é inferido ao atribuir o valor a mesma.
Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;
"""

numero = 42 # Exemplo de variável Global
print(numero)
print(type(numero))

novo = 0

if numero > 10:
    novo = numero + 10
    print(novo)  # A vaviável 'novo' esta declarada localmente dentro do bloco do if. Portanto, é local
print(novo)