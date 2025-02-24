#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input("Qual a velocidade:   "))
if velocidade <=80:
    print("Velocidade de {}KM dentro do limite, parabens".format(velocidade))
if velocidade >80:
    multa  = (velocidade-80)*7
   
    print("velocidade de {}KM acima do limite!!, devera pagar uma multa de {}R$".format(velocidade,multa)) 
    