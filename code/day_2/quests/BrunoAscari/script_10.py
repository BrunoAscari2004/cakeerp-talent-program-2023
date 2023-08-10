'''10 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que
calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário
atual:
A. salários até R$ 280,00 (incluindo) : aumento de 20%
B. salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
C. salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
D. salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
E. o salário antes do reajuste;
F. o percentual de aumento aplicado;
G. o valor do aumento;
H. o novo salário, após o aumento.'''

salarios = [280, 500,1000, 1500,3000]
reajustados = []

for salario in salarios:
    if(salario <= 280):
        salario= salario *1.2
        reajustados.append(salario)
    elif(salario<700):
        salario = salario*1.15
        reajustados.append(salario)
    elif(salario<1500):
        salario = salario*1.1
        reajustados.append(salario)
    elif(salario>=1500):
        salario = salario*1.05
        reajustados.append(salario)

for i in range(0,5):
    print(f"\nO salario {i} antes do reajuste era {salarios[i]}")
    print(f"O percentual de aumento do salario foi de {(reajustados[i]/salarios[i])*100%100:.2f}%")
    print(f"O valor do aumento foi de {(reajustados[i]-salarios[i])} reais")
    print(f"O novo salario após o aumento é {reajustados[i]}")