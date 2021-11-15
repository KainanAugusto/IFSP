#Variáveis
cont = 0
vetor = [0]*5

#Código
for cont in range (0,5,1) :
    vetor[cont] = int(input("Informe o número para a posição " + str(cont) + " :" ))

for cont in range (0,5,1) :
    print(vetor[cont], end = '')
