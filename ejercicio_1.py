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