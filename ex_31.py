#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
print("-"*30)
distancia = float(input("Qual adistancia da viajem??"))
if distancia <=200:
    dinheiro=distancia*0.50
    print("O total da viajem de {}KM deu: {}R$".format(distancia,dinheiro))
if distancia >200:
    adinheiro=distancia*0.45
    print("O total da viajem de {}KM deu: {}R$".format(dinheiro,adinheiro))