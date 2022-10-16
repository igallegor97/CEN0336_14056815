import sys
import math

#print("\nArguments passed:", end = " ")
#for i in range(1, n):
#    print(sys.argv[i], end = " ")

#print(isinstance(float(sys.argv[1]), int))
#REVISAR
if type(int(sys.argv[1])) == int:
    print("Funcionaaaaaaa!!!")
else:
    print("No funcionaaaaaa")


#def is_integer_num(n)

if int(sys.argv[1]) < 0:       
    # exits the program 
    sys.exit("a es negativo")     
 
if int(sys.argv[2]) < 0:
    # exits the program 
    sys.exit("b es negativo")   

if int(sys.argv[1]) > 500:
    # exits the program 
    sys.exit("a es mayor de 500")

if int(sys.argv[2]) > 500:
    # exits the program 
    sys.exit("b es mayor de 500")





H=int(sys.argv[1])**2+int(sys.argv[2])**2

print("\n\nO quadrado da hipotenusa para o triangulo retângulo com lados a=" + str(sys.argv[1]) + " e b=" + str(sys.argv[2]) + " é:", H)
