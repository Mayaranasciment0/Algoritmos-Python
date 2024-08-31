#Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja “F” e 
#estado civil seja “CASADA”, solicitar o tempo de casada (anos). 

nome = input("Digite seu nome: ")
idade = int (input("Digite sua idade: "))
sexo = input ("Informe seu Sexo em forma de (F ou M)")
estadoCivil = input ("Informe seu estado civil (casado, solteiro ou divorciado)")

if sexo == "F" and estadoCivil == "casado":
    tempoDeCasamento = int (input ("Hà quanto tempo você está casado? "))
    print ("Nome", nome,", idade:", idade,", sexo:", sexo,", estado civil:", estadoCivil,", hà", tempoDeCasamento, "anos")
else:
    print ("Nome", nome, ", idade:", idade, ", sexo:", sexo, ", estado civil:", estadoCivil)