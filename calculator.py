print ("Calculadora em Python:")
numero1 = float(input("Digite o 1º numero: "))
operador = input("Digite o operador desejado: ")
numero2 = float(input("Digite o 2º numero: "))

if operador == "+":
    print("Resultado soma = ", (numero1+numero2))
elif operador == "-":
    print("Resultado subtração = ",(numero1-numero2))
elif operador == "*":
    print("Resultado multiplicação = ",(numero1*numero2))
elif operador == "/":
    print("Resultado divisão = ", (numero1/numero2))
else:
    print("Operador inválido")
