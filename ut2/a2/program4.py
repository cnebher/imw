import sys
import math

circumferenceR = float(sys.argv[1])

print('Radio de entrada: r= ', circumferenceR)


diameter  = 2 * circumferenceR

perimeter = 2 * math.pi * circumferenceR

area      = math.pi * circumferenceR ** 2

print('￮ Soluciones: ')

print('￮ Diámetro: ', diameter)

print('￮ Perímetro: ', perimeter)

print('￮ Área: ', area)
