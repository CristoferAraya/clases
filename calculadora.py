def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
 
  if b == 0:
        return "No se puede dividir por cero"
  else:
     resultado = a / b
     return resultado
  
def obtenerNumero(texto):
    while True:
        try:
          
         numero =float(input(texto))
         if numero == 0:
             print("Debes ingresar un numero mayor a 0")
             continue
         
         return numero
        except:
            print("Debes ingresar un numero")
num1 = obtenerNumero("Primer número: ")
num2 = obtenerNumero("Segundo número: ")

resultadoSuma = sumar(num1, num2)
print("Suma: ",resultadoSuma)

resultadoResta= restar(num1, num2)
print("Resta: ", resultadoResta)

resultadoMultiplicacion = multiplicar(num1, num2)
print("Multiplicacion:", resultadoMultiplicacion)

resultadoDivision = dividir(num1, num2)
print("division:", resultadoDivision)