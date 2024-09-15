#Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em 
#P.A. contendo 10 valores. 

a = int(input("Digite o valor Inicial (A):"))

r = int(input("Digite o valor da Razão R:"))

print("Sequência em P.A com 10 valores:")
for n in range(10) :
    an = (a + n) * r
    print(an)