# Faça um algoritmo para receber um número qualquer e informar na tela se é par ou ímpar

valor = int(input("Digite um qualquer número: "))

if valor % 2 == 0:
    print(" O número", valor, " é par")
else:
    print("O número", valor, " é impar")