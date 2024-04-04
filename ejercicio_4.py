import time #importa la libreria de time para calcular cuanto tarda en ejecutar un conjunto de pasos en el código
t_significativo : int = 10 # se toma como tiempo significtivo para calcular un valor mas de 10 segundos
# se define la función recursiva para calcular la serie de Fibonacci
def fibo_recursivo(n : int )-> int: # se usa como argumento el término de la serie al que se desea llegar
    if n <=1:
        # CASO BASE
        return 1
    else:
        # CONDICION
        return fibo_recursivo(n-1)+fibo_recursivo(n-2)
    
# se define la funcion para calcular la serie de Fibonacci con iteración   
def fibo_iterativo(n : int )-> int: # se usa como argumento el termino de la serie al que se desea llegar (n)
    i : int = 1 # se declara la variable iteradora que contara los términos a lo que se avanza, iniciará en 1 (primer termino) y llegara hasta n
    # se declaran los dos primeros numeros con los que empezará la serie
    n1 : int = 0 
    n2 : int = 1
    while(i <= n): # mientras el numero del termino sea menor a n (el esperado), hacer
        sumFibo = n1 + n2
        n1 = n2
        n2 = sumFibo
        i += 1
    return sumFibo #retorna el valor final de la suma

if __name__ == "__main__":
    # dentro de un bucle, se va probando con cada numero cuando tarda en llegar a cada término de la serie de FIbonacci
    for i in range (1, 1000):
        # Calcula cuando tarda en calcular n termino de la serie la funcion recursiva
        start_time = time.time() 
        serieFibo = fibo_recursivo(i)
        end_time = time.time()
        timer = end_time - start_time
        print(f"La serie de Fibonacci recursiva hasta {i} es {serieFibo} y tarda {timer} segundos")

        # calcula cuando tarda en calcular n termino de la serie la funcion iterativa
        start_time2 = time.time()
        serieFibo = fibo_iterativo(i)
        end_time2 = time.time()
        timer2 = end_time2 - start_time2
        print(f"La serie de Fibonacci iterativa hasta {i} es {serieFibo} y tarda {timer2} segundos")

        if timer2 > t_significativo: # Si la funcion iterativa tarda mas de 10 segundos en calcular n termino, 
            print(f"la serie fibonacci iterativa tarda mas de 10 segundos en hallar el termino {i}")
            break # rompe el ciclo e imprime el resultado
        elif timer > 10: # Si la funcion recursiva tarda mas de 10 segundos en calcular n termino, 
            print(f"la serie fibonacci recursiva tarda mas de 10 segundos en hallar el termino {i}")
            break # rompe el ciclo e imprime el resultado
        else:
            continue