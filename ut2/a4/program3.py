import sys
import crayons

wordnumber = int(sys.argv[1])
word_as_list = sys.argv[2]
count_words = 0

if wordnumber < 0:
    print(crayons.red('Error, el número tiene que ser positivo'))
else:
    if wordnumber > 0 :
        word_as_list = word_as_list.split()
        for i in word_as_list:
            if len(i) == wordnumber:
                count_words += 1

    print(f'Hay {count_words} palabra(s) de tamaño {wordnumber}')
