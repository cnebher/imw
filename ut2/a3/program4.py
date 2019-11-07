import sys
import crayons

number = int(sys.argv[1])
finalvalue = 1

if number < 0:
    print(crayons.red('Error, el número tiene que ser positivo'))
else:
    for factorial in range(1, number + 1):
        finalvalue = finalvalue * factorial
        print(factorial, '! =', finalvalue)
