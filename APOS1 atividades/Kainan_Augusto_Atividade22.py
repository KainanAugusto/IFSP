#Variáveis
nota1 = 0.0
nota2 = 0.0
nota3 = 0.0
tipoM = ""
#Função
def media (n1,n2,n3,div):
    result = (n1+n2+n3) / div
    return result

#Programa principal
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
tipoM = input(" Informe o tipo de média. A para aritmética ou P para ponderada: ")

if tipoM == 'A':
    divisor = 3
    print("O resultado da média ARITMÉTICA é: ", str(media(nota1,nota2,nota3,divisor)))
else:
    if tipoM == 'P':
        nota1 = nota1*5
        nota2 = nota2*3
        nota3 = nota3*2
        divisor = 5+3+2
        print("O resultado da média PONDERADA é: ", str(media(nota1,nota2,nota3,divisor)))