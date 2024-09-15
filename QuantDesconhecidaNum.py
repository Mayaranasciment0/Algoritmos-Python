#Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles 
#estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve 
#terminar quando for lido um número negativo. 

valores = []
contagem1 = []
contagem2 = []
contagem3 = []
contagem4 = []

while True:
    valor = int(input("Digite um valor positivo para continuar ou negativo para encerrar"))

    if valor < 0:
        break

    valores.append(valor)

    if valor >= 0 and valor <= 25:
        contagem1.append(valor)
    elif valor >= 26 and valor <= 50:
        contagem2.append(valor)
    elif valor >= 51 and valor <= 75:
        contagem3.append(valor)
    elif valor >=76 and valor <= 100:
        contagem4.append(valor)
    else:
        print("Tente novament, digite um valor entre 0 e 100.")

quantidade_contagem1 = len(contagem1)
quantidade_contagem2 = len(contagem2)
quantidade_contagem3 = len(contagem3)
quantidade_contagem4 = len(contagem4)

print("Os valores inseridos foram: ", valores)
print("Quantidade de valores entre 0 e 25: ", quantidade_contagem1)
print("Quantidade de valores entre 26 e 50: ", quantidade_contagem2)
print("Quantidade de valores entre 51 e 75: ", quantidade_contagem3)
print("Quantidade de valores entre 76 e 100: ", quantidade_contagem4)
