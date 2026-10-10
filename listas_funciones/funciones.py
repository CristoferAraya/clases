# funciones sin parametro
def suma():
    print(1 + 1)

# funcion con parametro
def suma (x, y):
    print(x + y)

# funciones con parametros y retorno
def sumaRetorno(x, y):
    resultado = x + y
    return resultado

suma(2, 5) # <- llamada
suma(5, 6)

resultadoSuma = sumaRetorno( 2, 3)
print(resultadoSuma * 2)