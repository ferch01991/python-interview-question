def count_characters(s):
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)

word = input('Enter your string: ')
count_characters(word)

# administration
# {'a': 2, 'd': 1, 'm': 1, 'i': 3, 'n': 2, 's': 1, 't': 2, 'r': 1, 'o': 1}