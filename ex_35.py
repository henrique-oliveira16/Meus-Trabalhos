r1 = float(input("Qual o primeiro segmento: "))
r2 = float(input("Qual o segundo segmento: "))
r3 = float(input("Qual o terceiro segmento: "))
if r1< r2 +r3 and r2< r1+r3 and r3< r2+r1:
    print("Os lados formam um triangulo!!")
else:
    print("Os lados NÃO formam um trinagulo!!")