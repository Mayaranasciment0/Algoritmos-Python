# Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que 
# calcule seu peso ideal.

altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo em M ou F")

if sexo == "M":
   pesoIdeal = 72.2 * altura - 58
else:
   pesoIdeal = 62.1 * altura - 44.7

print ("o peso ideal é", pesoIdeal)