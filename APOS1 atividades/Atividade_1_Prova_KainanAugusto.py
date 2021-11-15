#Variáveis
maior = 0
menor = 999999
mediador = int

#Código
print("Informe quantos números queira.\nO programa dirá qual o maior e o menor número digitado.")
while mediador != 0 :
  mediador = int(input("Digite 0 para finalizar ou um número para continuar. "))
  if mediador >= maior :
    maior = mediador
  else :
      if mediador <= menor and mediador > 0 :
          menor = mediador

print("O maior número digitado foi: ", str(maior))
print("O menor número digitado foi: ", str(menor))