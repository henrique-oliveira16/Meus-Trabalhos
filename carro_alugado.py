dias = int(input("Qunatos dias o carro foi alugado?: ")) ## recebendo as informações
km = float(input("Quantos KM o carro rodou?: "))

total_d = dias*60## 60 reais por dia, sobre o aluguel do carro
total_km = km*0.15## 15 centavos por km rodado
valor_aluguel = total_d + total_km
print("O total a pagar de aluguel do carro é: {}R$".format(valor_aluguel))