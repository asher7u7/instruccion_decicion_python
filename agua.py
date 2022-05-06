"""ejercicio 5: programa para calcular el gasto de agua de una vivienda dado el número de m2 de agua
gastados"""

#input

metros_gastados=int(input("¿cuantos metros ha gastado?: "))
costo_agua=0

#procesing

if metros_gastados<=50:
    costo_agua=10000
else:
    if metros_gastados<=200:
        costo_agua=10000+2000*(metros_gastados-50)
    else:
         costo_agua=10000+3000*(metros_gastados-50)

#output

print("el costo a pagar por el agua utilizada es " + str(costo_agua))