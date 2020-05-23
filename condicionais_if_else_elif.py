"""
Estruturas condicionais
If, Else e Elif(else if)
"""

idade = 26

"""
# Estrutura condicional if e Else, no C

 if (idade < 18) {
 printf("Menor de idade)
} else if (idade == 18) {
 print("Tem 18 anos)
} else {
  printf("É menor de idade")
}
"""

"""
# Estrutura condicional if e Else, no Java

 if (idade < 18) {
 System.out.println("Menor de idade)
} else if (idade == 18){
print("Tem 18 anos")
} else {
  System.out.println("Maior de idade)
}
"""
if idade < 17:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
elif idade == 26:
    print('Tem 26 anos')
else:
    print('Maior de idade')

