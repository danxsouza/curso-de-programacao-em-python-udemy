"""
Tipo String
Em Python, um dado é considerado do tipo String, sempre que:
- Estiver entre àspas simples -> 'uma string', '234', 'a', 'true'
- Estiver entre àspas duplas -> "uma string", "234", "a", "true"
- Estiver entre àspas simples triplas -> '''uma string''', '''234''', '''a''', '''true'''
"""
# Estiver entre àspas duplas triplas -> """uma string"""", """234""", """a""", """true"""

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = """Anjelina
Jolie"""
print(nome)
print(type(nome))

nome = 'Geek University'
print(nome.upper())

print(nome.split()) #tranforma em uma lista de Strings

"""
[::-1] -> Começe do primeiro elemento, vá até o último elemento e INVERTA
"""
print(nome[::-1])
