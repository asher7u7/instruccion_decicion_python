"""ejercicio 4
programa que calcula el índice de masa corporal de una persona
e indica el estado en el que se encuentra esa
persona en función del valor del IMC."""


print("--------------------------------------------")
print("-------programa para calcular el IMC -------")
print("-----y indica el estado de la persona-------")
print("--------------------------------------------")

#input

peso=float(input("digite su peso en kilogramos: "))
altura=float(input("digite su altura en metros: "))

#procesing and output

IMC=(peso/(altura*altura))

if IMC<16:
    print("usted esta muy por debajo del peso apropiado \ncriterio de ingreso al hospital")
else:
    if IMC<17:
        print("usted esta algo por debajo de su peso apropiado \ntiene infrapeso")
    else:
        if IMC<18:
            print("usted esta algo por debajo de su peso apropiado \nusted está con bajo peso")
        else:
            if IMC<25:
                print("usted posee un peso apropiado \nes una persona saludable")
            else:
                if IMC<30:
                    print("usted  está un poco sobre su peso adecuado \nposee sobrepeso (obesidad grado I)")
                else:
                    if IMC<35:
                        print("usted está algo por encima de su peso adecuado \nusted tiene sobrepeso cronico (obesidad grado II) ")
                    else:
                        if IMC<40:
                            print("usted está bastante por encima de su peso apropiado \nposee obesidad premorbida (obesidad grado III)")
                        else:
                            if IMC>40:
                                print("rey usted necesita 3 ataudes \n posee obesidad morbida (obesidad grado IIII)")

print("su imc es " + str(IMC))