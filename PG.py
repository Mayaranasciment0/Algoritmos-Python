#Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em 
#P.G. contendo 10 valores.  

a = int(input("Digite o valor Inicial (A):"))

r = int(input("Digite o valor da Razão R:"))

print("Sequência em P.G com 10 valores:")

for n in range(10) :
    an = a * (r ** (n - 1))
    print(an)