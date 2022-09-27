# Palíndromos

# Luz Azul
# Ana
# Yo hago yoga hoy
# Anita lava la tina

# - Ejercicio: Escribir un programa que identifique si una palabra es un palíndromo

def palindromo(text):
    text = text.replace(' ','')
    text = text.lower()
    
    if (text[::] != text[::-1]):
        print("No es un palindromo")
    else:
        print("La palabra ingresada es un palindromo.")
    
inicio = """
Bienvenido al identificador de palíndromos

Ingrese la frase: """

frase = palindromo(input(inicio))
