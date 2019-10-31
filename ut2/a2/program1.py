import sys
from math import sqrt

dataa, datab, datac = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

print('Datos de entrada: ')
print(dataa)
print(datab)
print(datac)

print('Debe dar las soluciones: ')

if (datab ** 2) - (4*dataa*datac) < 0:
    print('No tiene solucion real')
elif dataa != 0:
    solutionx1 = (- datab + sqrt(datab ** 2 - 4 * dataa * datac)) / (2 * dataa)
    solutionx2 = (- datab - sqrt(datab ** 2 - 4 * dataa * datac)) / (2 * dataa)
    print('X1= ', solutionx1)
    print('X2= ', solutionx2)
elif dataa == 0:
    solutionx = -datac // datab
    print('La ecuación ya no es de segundo grado y su resultado es: ', solutionx)
