import sys
import crayons

entrya = int(sys.argv[1])
entryb = int(sys.argv[2])
mcd = 0

if entrya < 0 or entryb < 0:
    print(crayons.red('Error, el número tiene que ser positivo'))
else:
    if entrya < entryb:
        entrya = min
    for i in range(0, min + 1):
        mcd = entrya % entryb
        if entrya  == 0:
            print(mcd)
