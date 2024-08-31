#Escreva um algoritmo que lê dois valores booleanos (lógicos) e então determina se ambos são 
#VERDADEIROS ou FALSOS. 

def converter_entrada(entrada):
    entrada = entrada.strip().lower() #strip remove espaços de uma string e lower converte para minusculas
    return entrada == 'true'

valor_1 = input("Escolha entre (True ou False): ")
valor_2 = input("Escolha novamente entre (True ou False): ")

Valor1 = converter_entrada(valor_1)
valor2 = converter_entrada(valor_2)

if Valor1 and valor2:
    print("Os dois são verdadeiros")
elif not Valor1 and not valor2:
    print("Os dois são falsos")
else:
     print("Um é verdadeiro e o outro é falso")
