'''9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.'''

lista = []
for i in range(0,3):
    num = float(input("Digite um número: "))
    lista.append(num)

print("Números em ordem decrescente: \n")
for c in range(2,-1,-1):
    print(f'{lista[c]:.2f}',end=' ')