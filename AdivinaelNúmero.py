import random
print("Se va a generar un número aleatorio entero de entre 0 y 99.")
naleatorio = random.randint(0, 99)
nelegido = int(input("Introduce el número que crees que se ha generado: "))
if nelegido == SyntaxError:
    print("Por favor, introduzca un número entero.")
    nelegido = int(input("Introduce el número que crees que se ha generado: "))
intentos = 1
while nelegido != naleatorio:
    print("El número elegido no es el correcto.")
    if nelegido < naleatorio:
        print("El número generado es mayor al introducido.")
    else:
        print("El número generado es menor al introducido.")
    print("Vuelve a intentarlo.")
    intentos += 1
    nelegido = int(input("Introduce el número que crees que se ha generado: "))
if nelegido == naleatorio:
    print("Has acertado!!!")
    print("El número de intentos que has necesitado es " + str(intentos))