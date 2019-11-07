import sys
import crayons

number = int(sys.argv[1])

if number < 0:
    print(crayons.red('Error, el número tiene que ser positivo'))

else:
    for divisible in range(2, number):
        if number % divisible == 0:
            print('No es primo!')
            break
    else:
        print('Es primo!')
