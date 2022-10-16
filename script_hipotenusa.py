#Importar librerías
#Libreria sys: Sirve para manejar los argumentos de entrada
import sys
#Libreria math: Sirve para realizar operaciones matematicas
import math

# Comprobar que a y b sean positivos

if int(sys.argv[1]) < 0:
    sys.exit("a es negativo")

if int(sys.argv[2]) < 0:
    sys.exit("b es negativo")

# Comprobar que a y b sean enteros
if bool(sys.argv[1].isdigit()) is False:
        print("a no es un entero")
        sys.exit()

if bool(sys.argv[2].isdigit()) is False:
        print("b no es un entero")
        sys.exit()

# Comprobar que a y b sean menores que 500

if int(sys.argv[1]) > 500:
    sys.exit("a es mayor de 500")

if int(sys.argv[2]) > 500:
    sys.exit("b es mayor de 500")

# Calcular el cuadrado de la hipotenusa

H=int(sys.argv[1])**2+int(sys.argv[2])**2

print("\n\nO quadrado da hipotenusa para o triangulo retângulo com lados a=" + str(sys.argv[1]) + " e b=" + str(sys.argv[2]) + " é:", H)

