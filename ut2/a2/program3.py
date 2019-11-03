import sys
import crayons

note = float(sys.argv[1])

print()

if note < 0:
    print(crayons.red('La nota está definida entre 0 y 10'))
elif note <= 4:
    print('￮ Suspenso')
elif note <= 7:
    print('￮ Aprobado')
elif note <= 9:
    print('￮ Sobresaliente')
elif note == 10:
    print('￮ Matrícula de honor')
elif note > 10:
    print(crayons.red('La nota está definida entre 0 y 10'))

print()
