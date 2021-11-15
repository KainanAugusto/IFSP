#variaveis
nome = ""
vendas = 0.0
situacao = ""

#código
nome = input("Digite o nome do vendedor :" )
vendas = float(input("Digite o valor de vendas desse vendedor: "))

if(vendas >= 10000 and vendas < 50000):
      situacao = "ideais!"
else:
    if(vendas >= 50000):
      situacao = "ótimas!"
    else:
        situacao= "baixas!"

print(nome , "suas vendas são de ", str(vendas) , ", e elas estão " , situacao)