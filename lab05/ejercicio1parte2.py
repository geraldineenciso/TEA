try:
   entrada =input ("ingrese el nombre del archivo: ")
   archivo = open(entrada, "r", encoding="UTF-8")
   for linea in archivo:
       print(linea.upper())
except:
    print ("error, no existe el archivo")


