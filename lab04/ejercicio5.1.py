contador = 0
suma = 0
primerNumero = True
while True:
    try:
        numero = input("ingrese un número: ")
        if (numero == "salir"):
            break
        contador = contador + 1
        suma = suma + int (numero)
    except:
        print("dato erróneo")

print( "contador", contador)
print ("Suma", suma)
print ("Promedio", suma/contador)

