'''3 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
A. "Telefonou para a vítima?"
B. "Esteve no local do crime?"
C. "Mora perto da vítima?"
D. "Devia para a vítima?"
E. "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada
como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''

lista_perguntas = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?", "Devia para a vítima?","Já trabalhou com a vítima?"]

suspeita=0 

for pergunta in lista_perguntas:
    resp = str(input(f"{pergunta} [S/N]: ")).upper()[0]
    if resp == 'S':
        suspeita +=1 

if(suspeita < 2):
    print('\n\033[1;37mA pessoa é Inocente\033[m')
elif(suspeita == 2):
    print("\n\033[1;32mA pessoa é Suspeita\033[m")
elif(suspeita <= 4):
    print("\n\033[1;33mA pessoa é Cúmplice\033[m")
elif(suspeita ==5):
    print("\n\033[1;31mA pessoa é o Assassino\033[m")
