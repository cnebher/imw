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


# 4 invertir palabras
def reverse(text):
    text = text[::-1]
    return text

if __name__ == '__main__':
    text = sys.argv[1]
    print('Number of vowels:', num_vowels(text))
    print('Number of whitespaces:', num_whitespaces(text))
    print('Reverse of text:', reverse(text))
