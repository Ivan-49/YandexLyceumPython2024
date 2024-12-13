word = input()
len_slice = 0

if len(word) == 1:
    print(word)

while len(word) > 1:
    word = word[- (len(word) - len_slice):len(word) - len_slice]
    len_slice = 1
    print(word)