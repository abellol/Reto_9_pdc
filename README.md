# Reto 9: Funciones 2 (Recursivas, anónimas, *args)
### Soy Alejandro Bello y pertenezco al grupo de "Fenomenoides", adjunto nuestro logo: 

<details><summary>Preparense para ver el grandioso logo: </summary><p>
<div align='center'>
<figure> <img src="https://i.postimg.cc/NFbwf57S/logo-def.png" alt="Defensa Civil" width="400" height="auto"/></br>
<figcaption><b> "somos programadores, no diseñadores" </b></figcaption></figure>
</div>
</p></details><br>

### 1. De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.
#### En este caso tomé las funciones para calcular el área y perimetro de esta figura: 

[![image.png](https://i.postimg.cc/TwZ8H44y/image.png)](https://postimg.cc/sQ90Mwyy)

```python
from math import pi # Importo la libreria math para usar el valor de Pi
if __name__ == "__main__":

    # Se ingresan las medidas que desea el usuario de la figura 

    la_rect = float(input("ingrese el largo del rectangulo: "))
    an_rect = float(input("ingrese el ancho del rectangulo: "))
    radio = float(input("ingrese el radio de los circulos: "))

    # Con funciones anónimas (lambdas) se calcula el perimetro y area de cada figura

    area_rectangulo = (lambda x, y: x * y) (la_rect, an_rect)
    peri_rectangulo = (lambda x, y: 2 * x + 2 * y) (la_rect, an_rect)
    area_circulo = (lambda x: (x**2) * pi) (radio)
    peri_circulo = (lambda x: 2 * x * pi) (radio)

    # Se imprimen los valores calculados anteriormente

    print(f"el area del rectangulo de lados {la_rect} y {an_rect} es igual a {area_rectangulo}")
    print(f"el perimetro del rectangulo de lados {la_rect} y {an_rect} es igual a {peri_rectangulo}")
    print(f"el area del circulo de radio {radio} es de {area_circulo}")
    print(f"el perimetro del circulo de radio {radio} es igual a {peri_circulo}")
    print(f"el area total de la figura es de {area_rectangulo + 2 * area_circulo}")
```
### 2. De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).
#### Tomé las funciones para calcular media, promedio multiplicativo y mediana y las reescribí en funciones con argumentos por defecto
```python
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
```
### 3. Funcion recursiva para calcular la operación de la potencia
```python
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
```
### 4. Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa. (usando la plantilla de tiempo)
```python
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
```
## Cosas de adultos...
#### Acá está el enlace a mi cuenta en [Stackoverflow](https://stackoverflow.com/users/23997723/alejandro-bello-leon), además adjunto la imagen de mi perfil:
<details>
<summary>Prueba de perfil existente...</summary>

### Perfil de Stackoverflow
[![stackoverflow-ss.png](https://i.postimg.cc/jqg1qN83/stackoverflow-ss.png)](https://postimg.cc/fkdCB3QY)

</details>

#### Acá esta el enlace de mi perfil en [LinkedIn](https://www.linkedin.com/in/alejandro-bello-leon-9679032b6)




