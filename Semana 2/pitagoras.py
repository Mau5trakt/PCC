from math import sqrt


def pitagoras(a, b):
    hipotenusa = sqrt((a**2)+(b**2))
    print("The Hypotenuse is: "+str(hipotenusa))


pitagoras(5,9)
pitagoras(10,3)
pitagoras(15,7)
