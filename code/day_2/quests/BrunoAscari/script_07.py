'''7 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''


letra = str(input("Digite o sexo [M/F]: ")).upper()[0]
if letra == 'F':
    print("Feminino")
elif letra == 'M':
    print("Masculino")
else:
    print("Sexo Inválido")