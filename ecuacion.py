"""ejercicio 6
solucion de ecuaciones de segundo grado"""

#input
a=int(input("digite el valor de a: "))
b=int(input("digite el valor de b: "))
c=int(input("digite el valor de c: "))

#procesing

d=b*b-4*a*c

if d==0:
    X1= -b/2*a
    X2= -b/2*a
elif d>0:
    X1= (-b+d**0.5)/2*a
    X2= (-b-d**0.5)/2*a
elif d<0:
    X1= ((-b+(1**0.5)*(d**0.5))/2*a)
    X2= ((-b-(1**0.5)*(d**0.5))/2*a)

#output

print("\nResultados\n")
print("X1 es igual a " +str(X1))
print("X2 es igual a " +str(X2))
