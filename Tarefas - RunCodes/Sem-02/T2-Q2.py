def RelAtr(x):
    horas = str(x)[:2]
    minutos = str(x)[3:]
    
    atraso = int(minutos)-3

    if atraso < 0:
        horaAtr = int(horas)-1
        minutosAtr = 60 + (atraso)
        return f"{horaAtr}:{minutosAtr}"
    else:
        return f"{horas}:{atraso}"


hour = input("Digite a hora, no formato XX:XX\n➥ ")
atras = RelAtr(hour)
Rhour = print(f"A hora no 'relógio que atrasa' é de {atras}")
