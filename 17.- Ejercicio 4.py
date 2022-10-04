# Ejercicio 4: Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

def main():
    for tabla in range(1,11):
        for linea in range(1, 13):
            cadena = str(tabla) + " X " + str(linea) + " = " + str(tabla * linea)
            
            print(cadena)
        print("\n")
        
    

if __name__ == '__main__':
    main()