# Pedir al usuario una lista de números separados por comas
entrada = input("Introduce una lista de números separados por comas: ")

# Convertir la entrada en una lista de enteros
lista_numeros = [int(x.strip()) for x in entrada.split(",")]

def sum_last_two_numbers(numeros):
    # Ordenar la lista en orden ascendente
    numeros.sort()
    lenght: int = len(numeros)

    # Verificar que hay al menos dos números
    if lenght < 2:
        print("Se necesitan al menos dos números.")
        return
    
    # Sumar los dos últimos números (los más grandes)
    resultado: int = numeros[lenght - 1] + numeros[lenght - 2]

    print("The result is:", resultado)


# Llamar la función con la lista procesada
sum_last_two_numbers(lista_numeros)