print("Este programa revisa si una palabra o frase es un palindromo o no")
palabra =input("ingresa la palabra o frase a revisar: ")

def palindromo(palabra:str):
    #elimina los espacios
    palabra = palabra.lower().replace(" ", "")
    resultado: str = ""
    # invierte la palabra o frase
    for letra in palabra:
        resultado: str = letra + resultado
    # revisa si la palabra o frase es un palindrom
    if palabra == resultado:
        print("la plabra o frase es un palindromo")
    else:
        print("la palabra o frase no es un palindromo")


# Llamar la función con la palabra o frase
palindromo(palabra)


"""
explicacion

Se toma la palabra del usuario y se escribe en minúsculas.
Luego, se invierte usando una cadena vacía para mostrar el resultado. 
Se realiza una comparación para ver si esa palabra es igual a la original.
"""