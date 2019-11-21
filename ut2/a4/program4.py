import sys

numbers = sys.argv[1:]
number = len(numbers)
count_number = 0

for seccion in numbers:
    seccion = float(seccion)
    count_number += seccion
result = count_number / number
print(f"La media de los valores es: {result}")
