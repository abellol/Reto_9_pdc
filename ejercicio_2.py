# se define la función de media con argumentos por defecto
def media (*args):
    suma : int = 0 # se inicia con la variable que acumulara la suma, empieza en 0 (módulo de la suma)
    for i in args: # para cada elemento en *args
        suma += i # a la suma se le suma el valor i dentro de args
    return (suma / (len(args))) # la función retorna la división de la suma total, entre el numero de operandos

# se define la funcion de promedio multiplicativo con argumentos por defecto
def promedio_multipli(*args):
    producto : int = 1 # se inicia con la variable que acumulara el producto, empieza en 1 (módulo de la multiplicación)
    for i in args: # para cada elemento en *args
        producto *= i # se multiplica el numero i por el producto anterior o inicial
    return producto ** (1/len(args)) # la funcion retorna la raiz de la cantidad de operandos del producto 

# se define la función de potencia de extremos con argumentos por defecto
def potencia_extremos(*args):
    sorted(args) # se ordena ascendentemente todos los numeros contenidos en *args
    x = args[len(args)-1] # dentro de una variable se almacena el numero mayor dentro de *args
    y = args[0] # dentro de otra variable se almacena el numero menor dentro de *args
    return x ** y # la funcion retorna el mayor elevado al menor  
 
if __name__ == "__main__":

    # el usuario ingresa n datos, en este caso 5

    a = int(input("Ingrese numero a: "))
    b = int(input("Ingrese numero b: "))
    c = int(input("Ingrese numero c: "))
    d = int(input("Ingrese numero d: "))
    e = int(input("Ingrese numero e: "))

    # se imprime lo que retorna cada función con los datos ingresados por el usuario (se usan los 5, no es obligatorio)
    print(f"la media de todos los numeros es: {media(a, b, c, d, e)}")
    print(f"la media de todos los numeros es: {media(a, b, c, d)}") # aca solo se usan 4 y no hay ningún error
    print(f"el promedio multiplicativo de todos los numeros es: {promedio_multipli(a, b, c, d, e)}")
    print(f"la potencia del mayor elevado al menor es: {potencia_extremos(a, b, c, d, e)}")