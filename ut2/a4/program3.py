import sys
import crayons

wordnumber = int(sys.argv[1])
word_as_list = sys.argv[2]
suma = 0

if wordnumber < 0:
    print(crayons.red('Error, el número tiene que ser positivo'))
else:
    if wordnumber > 0 :
        word_as_list = word_as_list.split()
        for i in word_as_list:
            len(i) == wordnumber
            print(f'Hay {wordnumber} palabra(s) de tamaño {wordnumber}')
