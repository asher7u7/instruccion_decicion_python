"""ejercicio 3: 
El dueño de una papelería desea un programa que le indique el precio de venta
de un articulo dado"""

print("------------------------------------------------------------------------")
print("--------programa para calcular el precio de venta de un producto--------")
print("------------------------------------------------------------------------")

#input

costoproducto=int(input("ingrese el costo de compra de su producto: "))
preciofinal=0
#procesing 

if costoproducto<3000:
    preciofinal= 15*costoproducto/100 + costoproducto
else:
    if costoproducto<=6000:
        preciofinal= costoproducto+500
    else:
        preciofinal= 25*costoproducto/100 + costoproducto

#output

print("el precio de venta de su producto es: " + str(preciofinal))
    