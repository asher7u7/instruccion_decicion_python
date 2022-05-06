"""ejercicio 2:
Programa que permita realizar un préstamo bancario, teniendo en cuenta que el
préstamo será otorgado solamente a personas con ingresos superiores a $945200
y que no posea ninguna otra deuda"""



print("------------------------------------------------------")
print("programa para ver si es apto para un prestamo bancario")
print("------------------------------------------------------")

#input, procesing and output

ingresos=int(input("¿cuanto son sus ingresos?: "))
if ingresos<945200:
     print("no es apto para recibir el prestamo")
else:
    deudas=int(input("¿tiene alguna deuda? 1)si. 2)no.: "))
    if deudas==2:
        print("si es apto para recibir el prestamo")
    else:
        print("no es apto para recibir el prestamo")
