#Faça um algoritmo que leia os valores A, B, C e 
# imprima na tela se a soma de A + B é menor que C

a = int (input("Digite o valor de A: "))
b = int (input("Digite o valor de B: "))
c = int (input("Digite o valor de C: "))

soma = a + b

if soma < c:
    print("Soma dos valores de A mais B é menor que C.")
else:
    print("A soma de A e B não é menor que C.")

