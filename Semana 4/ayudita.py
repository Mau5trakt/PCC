sentence = "hola soy german"
a =(sentence.split())#convierto el string a lista
b = len(a)
# print(len(a))
n = int(input("Ingrese que palabra de la frase desea obtener"))
if b > n and b < 0:
    print("")
elif n >1 and n <= b:
    c = a[n-1]
    print(c)
