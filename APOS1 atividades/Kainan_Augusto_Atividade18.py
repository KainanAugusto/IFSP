#Variaveis
contador = 0
numero = 0
maior = 0
mediador = 0

#Código
numero = int(input("Digite quantos números serão inseridos: "))

for contador in range (0 , numero , 1):
   mediador = int(input("Informe um número: "))
   if  mediador > maior  :
    maior = mediador

print("O maior número digitado foi: " , str(maior))