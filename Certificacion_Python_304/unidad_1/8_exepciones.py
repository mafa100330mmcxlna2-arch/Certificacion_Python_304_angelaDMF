#Ejemplo 1 sin manejo de excepciones

try:
    numero1=float(input("Ingresa el primer numero"))
    numero2=float(input("Ingresa el segundo numero"))
    resultado=numero1/numero2
    print(resultado)
except ZeroDivisionError:
     print("Error:No se puede dividir entre cero")
except ValueError:
    print("Error:No se puede ingresar letras")
 
