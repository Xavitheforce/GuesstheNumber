import random
numero = random.randint(0, 100)
print("Introduzca el número a adivinar")
while True:
    numero = input("Introduzca un número entre 0 y 99 incluídos: ")
    try:
        numero = int(numero)
    except:
        pass
    else:
        if 0 <= numero <= 99:
            break

print("intente encontrar el número a adivinar")
while True:
    while True:
        intento = input("Introduzca un número entre 0 y 99 incluídos: ")

        try:
            intento = int(intento)
        except:
            pass
        else:
            if 0 <= intento <= 99:
                break

    if intento < numero:
        print("Demasiado pequeño")
    elif intento > numero:
        print("Demasiado grande")
    else:
        print("Victoria!")
        break