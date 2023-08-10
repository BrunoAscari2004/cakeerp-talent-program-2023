'''6 - Faça um Programa que peça dois números e imprima o maior deles.'''

num1= int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

if num1>num2:
    print(num1)
elif num1<num2:
    print(num2)
else:
    print("Os numeros são iguais")