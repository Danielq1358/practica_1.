def multiplica_por_2(n):
    # Usamos range hasta n+1 para incluir el número, saltando de 2 en 2
    return list(range(0, (n * 2) + 1, 2))

# Test: [0, 2, 4, 6, 8, 10]
print(multiplica_por_2(5))

def suma_y_resta(lista):
    suma = lista[0] + lista[1]
    resta = lista[0] - lista[1]
    print(suma)
    return resta

# Test: Imprime 235, retorna 5
resultado = suma_y_resta([120, 115])

def sumatoria_menos_longitud(lista):
    suma_total = sum(lista)
    longitud = len(lista)
    return suma_total - longitud

# Test: 25 - 4 = 21
print(sumatoria_menos_longitud([10, 5, 3, 7]))

def valores_multiplicados_segundo(lista):
    if len(lista) < 2:
        print(len(lista))
        return []
    
    segundo_valor = lista[1]
    nueva_lista = [x * segundo_valor for x in lista]
    print(len(nueva_lista))
    return nueva_lista

# Test 1: Imprime 4, retorna [300, 9, 150, 60]
print(valores_multiplicados_segundo([100, 3, 50, 20]))

# Test 2: Imprime 1, retorna []
print(valores_multiplicados_segundo([100]))


def valor_multiplicado_longitud(valor, longitud):
    producto = valor * longitud
    return [producto] * longitud

# Test 1: [10, 10]
print(valor_multiplicado_longitud(5, 2))

# Test 2: [35, 35, 35, 35, 35]
print(valor_multiplicado_longitud(7, 5))