metro = int(input("Digite uma unidade em metros:"))
# Converte as unidades 
milimetro = metro * 1000
centimetro = metro * 100
decimetro = metro * 10
decametro = metro/10
hectometro = metro/100
quilometro = metro/1000
# apresenta a saida de dados/valor
print(f"O valor de {metro} m em milímetros é {milimetro} mm.")
print(f"O valor de {metro} m em centímetros é {centimetro} cm.")
print(f"O valor de {metro} m em decímetros é {decimetro} dm.")
print(f"O valor de {metro} m em decâmetros é {decametro:.2f} dam.")
print(f"O valor de {metro} m em hectômetros é {hectometro:.2f} hm.")
print(f"O valor de {metro} m em quilômetros é {quilometro:.3f} km.")





