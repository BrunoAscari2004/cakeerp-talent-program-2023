'''Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem
lida.'''

idade = []
altura = []

for c in range(0,3):
    idad = int(input(f"Digite a idade {c}: "))
    alt = float(input(f"Digite a altura {c}: "))
    idade.append(idad)
    altura.append(alt)

for i in range(2,-1,-1):
    print(f"Idade {i}: {idade[i]}")
    print(f"Altura {i}: {altura[i]}")