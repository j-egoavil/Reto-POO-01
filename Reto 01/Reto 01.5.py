print("Este programa hace operaciones basicas")


def filtrar_anagramas(lista):
    # crea un diccionario vacio
    grupos = {}
    # Agrupar palabras por sus letras ordenadas
    for palabra in lista:
        clave = "".join(sorted(palabra.lower()))
        if clave in grupos:
            grupos[clave].append(palabra)
        else:
            grupos[clave] = [palabra]
    # Mantener solo los grupos con más de un elemento
    resultado = []
    for grupo in grupos.values():
        if len(grupo) > 1:
            resultado.extend(grupo)
    return resultado


entrada = input("Introduce palabras separadas por comas: ")
# permita la entrada de varios datos
palabras = [p.strip() for p in entrada.split(",")]


anagramas = filtrar_anagramas(palabras)
print("Palabras que son anagramas:", anagramas)


"""
explicacion

se crea un diccionario vacio en el cual se van a ir ingrasando las claves
que son las palabras organizadas para luego comparar con el resto de palabras
para revisar si son anagramas
"""