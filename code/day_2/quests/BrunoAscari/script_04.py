"""4 - Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três armentos"""

def soma (a,b,c):
    somar = a+b+c
    return somar 

numeros = []

for i in range(0,3):
    num = int(input("Digite um numero: "))
    numeros.append(num)

res=soma(numeros[0],numeros[1],numeros[2])
print(res)