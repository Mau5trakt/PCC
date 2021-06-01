"""
use of the diferent string methods on
pyhton
"""
#Count
var1 = "Quisiera Saber Cuantas Veces Se Repite La Letra E En Esta Cadena De Caracteres"
var1 = var1.lower()
print(var1.count("e"))
#lower and upper
print(var1.upper())
print(var1.lower())
#endswith saber si una cadena termina con el valor que le insertamos
print(var1.endswith("res"))
print(var1.endswith("restop"))
#isnumeric -> Saber si una variable es meramente numérica o no
print(var1.isnumeric())
var2= "12345"
print(var2.isnumeric())
#join
a = "este es otro ejemplo"
print(a.split()), print(type(a))

