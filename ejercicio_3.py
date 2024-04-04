# se define la función recursiva para calcular la potencia
def potencia_recursiva ( x : float, n = int): # sus argumentos son una base (real) y un exponente (entero)
    suma : float = 1  # se inicia con la variable que acumulara el producto, empieza en 1 (módulo de la multiplicación)
    if n == 0: # si el exponente es igual a 0,
        # CASO BASE 
        return 1 # devuelve 1 como resultado
    elif n > 0: # si el exponente es mayor que 1 (positivo)
        suma *= x # al producto acumulado (inicialmente 1) se le multiplica por la base (x)
        # CONDICION
        return suma * potencia_recursiva(x, n-1) # se retorna el valor del producto acumulado multiplicado por la funcion de potencia recursiva con el exponente original restado en 1 (n-1)
    else: # si el exponente es menor que 1 (negativo)
        suma *= x  # al producto acumulado (inicialmente 1) se le multiplica por la base (x)
        # CONDICION
        return 1 / (suma * potencia_recursiva(x, -n-1))  #se retorna el valor1 dividido entre el producto acumulado multiplicado por la funcion de potencia recursiva con el exponente original restado en 1 (-n-1)

        
if __name__ == "__main__":

    # el usuario ingresa la base y exponente que desea calcular 
    x = float(input("ingrese la base de la expresion:  "))
    n = int(input("ingrese el exponente de la expresión:  "))

    # se imprime el resultado de lo que calcula la función con los datos ingresados por el usuario
    
    print(f"el valor de {x} elevado a {n} es igual a {potencia_recursiva(x,n)}")
