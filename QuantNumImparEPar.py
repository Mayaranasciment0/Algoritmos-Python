#Faça um algoritmo estruturado que leia uma quantidade não determinada de números positivos. 
#Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos 
#números lidos. O número que encerrará a leitura será zero. 

valores = []
pares = []
impares = []

while True:
    valor = int(input("Digite um valor positivo (ou 0 para encerrar): "))

    if valor == 0:
        break

    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    
    valores.append(valor)

soma_pares = sum(pares)
soma_valores = sum(valores)
quantidade_valores = len(valores)
quantidade_pares = len(pares)
quantidade_impares = len(impares)

media_pares = soma_pares / quantidade_pares if quantidade_pares > 0 else 0
media_valores = soma_valores / quantidade_valores if quantidade_valores > 0 else 0

print("Os valores inseridos foram:", valores)
print("A quantidade de números pares é:", quantidade_pares)
print("A quantidade de números ímpares é:", quantidade_impares)
print("A média geral dos valores é:", media_valores)
print("A média dos números pares é:", media_pares)
