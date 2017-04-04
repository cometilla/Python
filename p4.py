import sys

print ("Numero de argumentos", len(sys.argv))

suma = 0
hasta = len(sys.argv) - 1
for i in range(hasta):
    suma = suma + int(sys.argv[i+1])

print ("Suma: ", suma)

#Ahora por pantalla

valor = 1
suma = 0
while valor > 0:
    try:
        valor = int(input("0 = Fin  Entero a sumar: "))
        suma = suma + valor
    except:
        print("Solo numeros, por favor")
        valor = 1
    finally:
        print("Sigue sumando, o no")

print ("Suma: ", suma)
            