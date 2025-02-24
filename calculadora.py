
print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
opcao = int(input("Digite o número da opção desejada:"))


if(opcao == 1):
    num1 = int(input("Qual o primeiro número? "))
    num2 = int(input("Qual o segundo número? "))
    resultado = num1 + num2
    print("O resultado da soma de {} + {} = {}".format(num1, num2, resultado))
if(opcao == 2):
    num1 = int(input("Qual o primeiro número? "))
    num2 = int(input("Qual o segundo número? "))
    resultado = num1 - num2
    print("O resultado da subtração de {} - {} = {}".format(num1, num2, resultado))
if(opcao == 3):
    num1 = int(input("Qual o primeiro número? "))
    num2 = int(input("Qual o segundo número? "))
    resultado = num1 * num2
    print("O resultado da multiplicação de {} X {} = {}".format(num1, num2, resultado))
if(opcao == 4):
    num1 = int(input("Qual o primeiro número? "))
    num2 = int(input("Qual o segundo número? "))
    resultado = num1 / num2
    print("O resultado da divisão de {} / {} = {}".format(num1, num2, resultado))
