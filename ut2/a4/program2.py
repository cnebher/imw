import random

NUCLEOBASES = "ATGC"
DNA_SIZE = 100

sequence = ''.join([random.choice(NUCLEOBASES) for i in range(DNA_SIZE)])

adenine = 0
thymine = 0
guanine = 0
cytosine = 0

for char in sequence:
    if char == "A":
        adenine += 1
    elif char == "T":
        thymine += 1
    elif char == "G":
        guanine += 1
    elif char == "C":
        cytosine += 1

print(f'Adenine:  {adenine}')
print(f'Thymine:  {thymine}')
print(f'Cytosine: {cytosine}')
print(f'Guanine:  {guanine}')
