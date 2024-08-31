#Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá se 
#somar os dois, caso contrário multiplique A por B. Ao final de qualquer um dos cálculos deve-se 
#atribuir o resultado para uma variável C e mostrar seu conteúdo na tela.

valor_A = int (input ("Digite um valor: "))
valor_B = int (input ("Digite outro valor: "))

if valor_A == valor_B:
    valor_C = valor_A + valor_B
else:
    valor_C = valor_A * valor_B

print ("O resultado é", valor_C)