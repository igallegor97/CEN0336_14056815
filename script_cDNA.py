# cargo librerias
import sys
import re

# nombrar variables
SEQ = sys.argv[1]
n1 = sys.argv[2]
n2 = sys.argv[3]
n3 = sys.argv[4]
n4 = sys.argv[5]

# PARA n1
if bool(n1.isdigit()) is False:
	print("n1 no es un entero")
	sys.exit()
if int(n1) > len(SEQ):
        print("n1 es mayor que la longitud de la secuencia de ADN")
        sys.exit()

# PARA n2
if bool(n2.isdigit()) is False:
        print("n2 no es un entero")
        sys.exit()
if int(n2) > len(SEQ):
        print("n2 es mayor que la longitud de la secuencia de ADN")
        sys.exit()

# PARA n3
if bool(n3.isdigit()) is False:
        print("n3 no es un entero")
        sys.exit()
if int(n3) > len(SEQ):
        print("n3 es mayor que la longitud de la secuencia de ADN")
        sys.exit()

# PARA n4
if bool(n4.isdigit()) is False:
        print("n4 no es un entero")
        sys.exit()
if int(n4) > len(SEQ):
        print("n4 es mayor que la longitud de la secuencia de ADN")
        sys.exit()

# CDS1
#  extraer cds 1 teniendo en cuenta comienza a contar desde 0
cds1=SEQ[int(n1)-1:int(n2)]
# compruebo que el cds exraido comienza con ATG usando la funcion startswith
if bool(cds1.startswith("ATG")) is False:
	print("cds1 no empieza con ATG")
	sys.exit()

# CDS2
#  extraer cds 2 teniendo en cuenta comienza a contar desde 0
cds2=SEQ[int(n3)-1:int(n4)]
# compruebo que el cds exraido comienza con ATG usando la funcion startswith
if bool(cds2.endswith("TAG")) is True:
    print("cds2 termina con TAG: "+ cds2)
elif bool(cds2.endswith("TAA")) is True:
    print("cds2 termina con TAA: "+ cds2)
elif bool(cds2.endswith("TGA")) is True:
    print("cds2 termina con TGA: "+ cds2)
else:
    print("El cds no termina con TAG,TAA o TGA")
    sys.exit()
#Concatenar CDS1 y CDS2
print("La secuencia concatenada de cds1 y cds2 es: "+"\n" + cds1 + cds2)
