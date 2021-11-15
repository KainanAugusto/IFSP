#Variáveis
salario = 0.0
cheque1 = 0.0
cheque2 = 0.0
imposto = 0.0
saldo_conta = 0.0

#Algoritmo
salario = float(input("Qual o valor a ser depositado?"))
cheque1 = float(input("Qual o valor do primeiro cheque a ser emitido?"))
cheque2 = float(input("Qual o valor do segundo cheque a ser emitido?"))
imposto = ((cheque1 * 0.0038) + (cheque2 * 0.0038))

saldo_conta = (salario - cheque1 - cheque2 - imposto)
print("O saldo restante na conta é de ",str(saldo_conta), "reais" )