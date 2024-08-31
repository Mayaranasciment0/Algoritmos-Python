# Faça um algoritmo que leia uma variável e some 5 caso seja par ou some 8 caso seja ímpar, 
# imprimir o resultado desta operação.

valor = int(input("Digite um número: "))

if valor % 2 == 0:
    resultado = valor + 5
else:
    resultado = valor + 8

print("O resultado é:", resultado)
