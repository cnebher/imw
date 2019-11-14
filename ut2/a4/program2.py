import sys
import crayons

wordnumber = int(sys.argv[1])
word_as_list = sys.argv[2]
word_as_string = word_as_list.split(' ')

if wordnumber < 0:
    print(crayons.red('Error, el número tiene que ser positivo'))
else:
    if word_as_list.lengt == wordnumber:
        print(f'Hay word_as_list')
