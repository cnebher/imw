import sys

sentence = sys.argv[1]


def count_words(sentence):
    summary = {}
    sentence_list = sentence.split()
    for words in sentence_list:
        number = 1
        if words in summary:
            summary[words] = number + 1
        else:

            summary[words] = number

    return summary

for key, value in (count_words(sentence)).items():
    print(key, ":", value)
