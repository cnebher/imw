import sys
from math import sqrt

pointx1, pointy1 = float(sys.argv[1]), float(sys.argv[2])
pointx2, pointy2 = float(sys.argv[3]), float(sys.argv[4])
pointx3, pointy3 = float(sys.argv[5]), float(sys.argv[6])

print('Entrada: ')

print('')

print('(', pointx1, ',', pointy1, ')')
print('(', pointx2, ',', pointy2, ')')
print('(', pointx3, ',', pointy3, ')')

d1 = float(sqrt((pointx1 - pointx2) ** 2 + (pointy1 - pointy2) ** 2))
d2 = float(sqrt((pointx1 - pointx3) ** 2 + (pointy1 - pointy3) ** 2))

print('')

print('Salida: ')

print('')

print('El punto más cercano es', '(', pointx3, ',', pointy3, ')', ('a distancia'), d2)
