"""ejercicio 1: Programa que lea las coordenadas cartesianas (x, y) de un punto en el plano y
calcule el cuadrante al cual pertenece el punto. Si el punto está sobre un eje
también debe indicarlo"""

print("hola, esto es un Programa que lee las coordenadas cartesianas (x, y) de un punto en el plano y")
print("calcula el cuadrante al cual pertenece el punto. Si el punto está sobre eje tambien lo indica")

#input

coordenadasx=int(input("por favor ingrese coordenada de x: "))
coordenadasy=int(input("por favor ingrese coordenada de y: "))

#procesing and output

if coordenadasx>0 and coordenadasy>0:
    print("se encuentra en el primer cuadrante")
elif coordenadasx<0 and coordenadasy>0:
    print("se encuentra en el segundo cuadrante")
elif coordenadasx<0 and coordenadasy<0:
    print("se encuentra en el tercer cuadrante")
elif coordenadasx>0 and coordenadasy<0:
    print("se encuentra en el cuarto cuadrante")
elif coordenadasx==0:
    print("se encuentra sobre el eje y")
elif coordenadasy==0:
    print("se encuentra sobre el eje x")
