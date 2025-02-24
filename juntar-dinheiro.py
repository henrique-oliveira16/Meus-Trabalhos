deseja = "S"
if(deseja == "S"):
    print("----------------------------------")
    print("1- juntar 20%")
    print("2- juntar 25%")
    opcao = int(input("Qual opção você deseja?"))
    salario = float(input("Qual seu salário?"))
    tempo = int(input("Por quantos meses deseja guardar dinheiro?"))

if opcao == 1:
    total_juntado = 0  # Variável para armazenar o valor total acumulado
    for contador in range(tempo):  # O contador vai de 0 até tempo-1
        j = salario * 0.20  # Calcula 20% do salário
        total_juntado += j  # Acumula o valor juntado
    print(f"O valor juntado após {tempo} meses é: {total_juntado}")

