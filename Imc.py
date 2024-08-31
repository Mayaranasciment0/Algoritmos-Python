# Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição.

peso = float(input("Digite seu peso: "))
altura = float (input("Digite sua altura: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print("Está abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Está no peso normal")
elif imc > 25 and imc < 30:
    print("Está no acima do peso")
else:
    print("Está com obesidade")
