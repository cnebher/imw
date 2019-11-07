import sys
import crayons

entrya, entryb = int(sys.argv[1]), int(sys.argv[2])
mininfuntion = 0

if entrya < 0 or entryb < 0:
    print(crayons.red('Error, el número tiene que ser positivo'))

else:
    if entrya < entryb:
        mininfuntion = entrya
    else:
        mininfuntion = entryb

    for i in range(mininfuntion + 1, 0, -1):
        if entrya % i == 0:
            if entryb % i == 0:
                print(i)
                break
