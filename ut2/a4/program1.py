import sys
import crayons

num_dni = int(sys.argv[1])

letters = 'TRWAGMYFPDXBNJZSQVHLCKE'

dniletter = num_dni % 23

print(f'{num_dni}{letters[dniletter]}')
