"""5 - Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em
porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas."""

def somaImposto(taxaImposto,custo):
    precofinal = custo *(1+taxaImposto)
    return precofinal


imposto =10/100
produto = 500
res=somaImposto(imposto,produto)
print(res)