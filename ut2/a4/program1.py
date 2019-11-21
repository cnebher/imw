import sys
import crayons

num_dni = sys.argv[1]

letters = 'TRWAGMYFPDXBNJZSQVHLCKE'


if len(num_dni) == 8:
    num_dni = int(num_dni)
    dniletter = num_dni % 23
    letter = letters[dniletter]
    print(f'{num_dni}{letter}')
else:
    print(crayons.red('DNI no valido'))
