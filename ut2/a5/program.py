import sys

def num_vowels(text):
    num_vowels = 0
    for words in text.lower():
        if words in 'aeiou':
            num_vowels += 1
    return num_vowels

def num_whitespaces(text):
    num_whitespaces = 0
    for space in text:
        if space == ' ':
            num_whitespaces += 1
    return num_whitespaces

def num_digits(text):
    num_digits = 0
    for char in text:
        if char.isdigit():
            num_digits += 1
    return num_digits

def num_words(text):
    text_list = text.split()
    num_words = len(text_list)

    return num_words

def reverse(text):
    text = text[::-1]
    return text

def length(text):
    length = len(text)
    return length

def halfs(text):
    text_lenght = len(text)
    if text_lenght >= 2:
         mid = text_lenght // 2
         first = text[:mid]
         second = text[mid:]
    return ' | '.join([first, second])

def upper_vowels(text):
    vocals = ""
    for char in text:
        if char.upper() in "AEIOU":
            vocals += char.upper()
        else:
            vocals += char
    return vocals

def sorted_by_words(text):
    text_list = text.split()
    text = sorted(text_list)
    sorted_by_words = " ".join(text)
    return sorted_by_words

def length_of_words(text):
    mylist = []
    text_lenght = text.split()
    for word in text_lenght:
        mylist.append(str(len(word)))
    text_string = ' '.join(mylist)
    return text_string
if __name__ == '__main__':
    text = sys.argv[1]
    print('Number of vowels:', num_vowels(text))
    print('Number of whitespaces:', num_whitespaces(text))
    print('Number of digits:', num_digits(text))
    print('Number of words:', num_words(text))
    print('Reverse of text:', reverse(text))
    print('Length of text:', length(text))
    print('Halfs of text:', halfs(text))
    print('Text with uppercased vowels:', upper_vowels(text))
    print('Sorted by words:', sorted_by_words(text))
    print('Length of words:', length_of_words(text))
