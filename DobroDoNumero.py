#Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, 
#imprimindo o resultado. 

numero = int (input("Digite um valor: "))

if numero >= 0:
    resultado = numero * 2 
elif numero < 0:
    resultado = numero * 3 

print ("O resultado é ", resultado)