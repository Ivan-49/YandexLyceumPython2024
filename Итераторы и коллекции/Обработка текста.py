import string
from sys import stdin

punctuation_table = str.maketrans("", "", string.punctuation)

words = []
for i in stdin:
    words.extend(word.translate(punctuation_table) for word in i.split())

word_indices = {}
for index, word in enumerate(words):
    if word not in word_indices:
        word_indices[word] = index

sorted_words = sorted(word_indices.items())

for word, index in sorted_words:
    if word == word.capitalize():
        print(f"{index} - {word}")
