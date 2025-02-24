altura = float(input("Altura da parede: "))
largura = float(input("Largura da parede: "))

area = altura*largura

tinta = area/2

print("Para pinta uma pardede altura de :{}M e de {}M de largura, cuja a area e de: {}M², sera nescessario {}L de tinta".format(altura,largura,area,tinta))