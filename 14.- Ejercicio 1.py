#

def main():
    frase = input("Ingresa una frase: ")
    letra_a_buscar = input("Ingrese una letra: ")
    
    frase = frase.lower()
    letra_a_buscar = letra_a_buscar.lower()
    
    contador = 0
    for letra in frase:
        if letra == letra_a_buscar:
            # contador = contador + 1
            contador += 1
            
    print("La letra " + letra_a_buscar + " aparece: " + str(contador))
    
if __name__ == '__main__':
    main()