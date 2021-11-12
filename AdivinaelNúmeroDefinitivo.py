import sys
MIN = 0
MAX = 99

def pedir_numero(invitacion):
    while True: 
        entrada = input(invitacion) 
        try: 
            entrada = int(entrada)
        except:
            print("Solo estan autorizados los carácteres [0-9].", file = sys.stderr)
        else: 
            return entrada

def pedir_numero_limite(invitacion, minimo=MAX, maximo=MAX):
    while True:
        invitacion = "{} entre {} y {} incluidos ".format(invitacion, minimo, maximo)
        entrada = pedir_numero(invitacion) 
        if minimo <= entrada <= maximo: 
            return entrada

def jugar_una_vez(numero, minimo, maximo): 
    intento = pedir_numero_limite("Adivine el número", minimo, maximo) 
    if intento < numero: 
        print("Demasiado pequeño") 
        minimo = intento + 1 
        victoria = False 
    elif intento > numero: 
        print("Demasiado grande") 
        maximo = intento - 1 
        victoria = False 
    else: 
        print("¡Ha ganado!") 
        victoria = True 
        minimo = maximo = intento 
    return victoria, minimo, maximo

def pedir_numero_incognita():
    return pedir_numero_limite("Introduzca el número a adivinar", minimo, maximo)

def jugar_una_PARTIDA(numero, minimo, maximo):
    while True:
        victoria, minimo, maximo = jugar_una_vez(numero, minimo, maximo)
        if victoria:
            return

def decidir_limites():
    while True:
        minimo = pedir_numero("¿Cuál es el límite inferior? ")
        maximo = pedir_numero("¿Cuál es el límite superior? ")
        if maximo > minimo:
            return minimo, maximo

def jugar():
    minimo, maximo = decidir_limites()
    numero = pedir_numero_incognita()
    jugar_una_PARTIDA(numero, minimo, maximo)

jugar()