print("Este programa hace operaciones basicas")


def calcular(num_1:float, num_2:float, operacion:str):
     if operacion == "+":
        return num_1 + num_2
     elif operacion == "-":
        return num_1 - num_2
     elif operacion == "*":
        return num_1 * num_2
     elif operacion == "/":
        return num_1 / num_2
     
     
num_1 = float(input("Ingres el primer numero a operar (puede tener decimales): "))
num_2 = float(input("Ingres el segundo numero a operar (puede tener decimales): "))
operacion = str(input("Ingrese la operacion que desea realizar(+, - *, /): "))
resultado = calcular(num_1, num_2, operacion)
print(resultado)


""" 
explicacion

Se toman los dos números y la operación, y la operación a realizar se define según la 
entrada del usuario. Devuelve el valor de esa operación.
"""