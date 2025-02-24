a_salario = float(input("Qual é seu salario: "))
if a_salario > 1250:#caso for maior
    aumento = a_salario*0.10
    salario = aumento + a_salario
    print("Seu salario anterior é de {}R$ o atual é  {}R$".format(a_salario,salario))
if a_salario <=1250:
    aumento = a_salario*0.15
    salario = aumento+a_salario
    print("Seu salario anterior é de {}R$ o atual é  {}R$".format(a_salario,salario))