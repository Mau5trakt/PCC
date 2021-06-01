from datetime import datetime

definir_dia = (datetime.today().weekday())
if definir_dia == 0:
    print("Hoy es Lúnes")

elif definir_dia == 1:
    print("Hoy es Martes")

elif definir_dia == 2:
    print("Hoy es Miércoles")

elif definir_dia == 3:
    print("Hoy es Jueves")

elif definir_dia == 4:
    print("Hoy es Viernes")

elif definir_dia == 5:
    print("Hoy es Sábado")

elif definir_dia == 6:
    print("Hoy es Domingo")