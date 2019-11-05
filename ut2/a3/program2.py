import sys
import crayons

number = int(sys.argv[1])
valve = 0

if number < 0:
    print(crayons.red('Error, el número tiene que ser positivo'))
else:
    for i in range(1, number + 1):
        valve += i ** 2
    print(valve)
