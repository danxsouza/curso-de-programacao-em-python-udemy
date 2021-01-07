"""
Funções com parâmeto (de entrada)
- Funções que recebem dados para serem processadas dentro da mesma;

Se a gente pensar em programa qualquer, geralmente temos:

entrada -> processamento  -> saida

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possueme entrada;
- Nãõ possuem saida;
- Possuem entrada mas nao possuem saida;
- Nao possuem entrada mas possuem saida;
- Possuem entrada e saida;


def quadrado(numero):
    return numero * numero

print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
#print(quadrado()) # Vai dar um erro de Type Error por não ter um valor dentro da funçao
print(ret)

def cantar_parabens(aniversariante):
    print('Parabéns para você')
    print('Nesta data tão querida')
    print('Muitas felicidades')
    print(f'Viva o {aniversariante}')

    cantar_parabens('Danilo')


def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2,2))
print(soma(2,5))

print(multiplica(2, 8))

print(outra(3, 2, 'Geek '))
print(outra(5, 3, 'Universiy '))


def nome_completo(nome, sobrenome):
    return f'Seu nome completo é: {nome} e seu sobrenome é: {sobrenome}'

print(nome_completo('Danilo', 'Batista'))

nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(nome, sobrenome))

"""
# Refatorando uma funçao


def soma_impares(numero):

    total = 0
    for num in numero:
        if num % 2 != 0:
            total = total + num
    return total

lista =  [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))
