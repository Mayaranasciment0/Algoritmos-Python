# Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem 
# decrescente. 

valorA = int (input("Digite o primeiro valor: "))
valorB = int (input("Digite o segundo valor: "))
valorC = int (input("Digite o terceiro valor: "))

valores = [valorA, valorB, valorC]

valores.sort(reverse=True)

print("Os valores em ordem decrescente são: ", valores)