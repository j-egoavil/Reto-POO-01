print("este programa revisa si un numero es primo")


def es_primo(numero):
    # el primo menor es 2 por lo que culaquier numero anterior no lo es
    if numero < 2:
        return False
    # calcula si el numero es primo o no 
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


# crea una lista con los numeros que sean primos
def filtrar_primos(lista):
    return [num for num in lista if es_primo(num)]


entrada = input("Introduce una lista de números separados por comas: ")
# permita la entrada de varios datos
lista_numeros = [int(x.strip()) for x in entrada.split(",")]
primos = filtrar_primos(lista_numeros)
print("Números primos encontrados:", primos)


"""
explicacion

Se toma la lista de números y se elimina el 1 si está presente.
Se comprueba si cada número es primo comprobando su divisibilidad desde 2 hasta el número menos uno.
Si un número es divisible, no es primo y el bucle se interrumpe. Si no se encuentran divisores,
el número se añade a la lista de primos, que luego se imprime.
"""