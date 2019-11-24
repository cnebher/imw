import sys

# 1 numero vocales
def num_vowels(text):
    num_vowels = 0
    for char in text.lower():
        if char in 'aeiou':
            num_vowels += 1
    return num_vowels
# 2 numero de espacios
def num_whitespaces(text):
    num_whitespaces = 0
    for char in text:
        if char == ' ':
            num_whitespaces += 1
    return num_whitespaces
# 3 numero de digitos
def num_digits(text):
    num_digits = 0
    for char in text:
        if char.isdigit():
            num_digits += 1
    return num_digits
# 4 numero de palabras
def num_words(text):
    text_list = text.split()
    num_words = len(text_list)

    return num_words
# 5 invertir palabras
def reverse(text):
    text = text[::-1]
    return text
# 6 longitud
def length(text):
    leng = len(text)
    return leng
# 7 mitad
# 8 vocales mayus
def upper_vowels(text):
    vocals = ""
    for char in text:
        if char.upper() in "AEIOU":
            vocals += char.upper()
        else:
            vocals += char
    return vocals
# 9 palabras ordenadas
def sorted_by_words(text):
    text_list = text.split()
    text = sorted(text_list)
    sorted_by_words = " ".join(text)
    return sorted_by_words
# 10 longitud de palabras
if __name__ == '__main__':
    text = sys.argv[1]
    print('Number of vowels:', num_vowels(text))
    print('Number of whitespaces:', num_whitespaces(text))
    print('Number of digits:', num_digits(text))
    print('Number of words:', num_words(text))
    print('Reverse of text:', reverse(text))
    print('Length of text:', length(text))
    #print('Halfs of text:', halfs(text))
    print('Text with uppercased vowels:', upper_vowels(text))
    print('Sorted by words:', sorted_by_words(text))
    #print('Length of words:', length_of_words(text))
