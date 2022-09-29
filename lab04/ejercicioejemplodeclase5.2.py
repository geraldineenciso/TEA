def imprimirNúmero(número):
    if (número == 1):
        mensaje = "uno"
    elif (número == 2):
        mensaje = "dos"
    elif (número == 3):
        mensaje = "tres"
    else:
        mensaje = "No definido"
    return mensaje
    
while True:
    número = input("Ingrese un número: ")
    if (número == "salir"):
        break
    numeroletras = imprimirNúmero(int(número))
    print(numeroletras)

