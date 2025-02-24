valor = float(input("Qual o valor do produto? R$:  "))
desconto  = valor*0.05
resultado = valor-desconto
print("O valor do produto era {}R$ após o desconto de 5%, o valor tornou-se {}R%".format(valor,resultado))