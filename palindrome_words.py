""" Program for know if a text is palindrome or not"""

def palindrome_words(sentence):
    """Function for the say if the sentence is palindrome or not"""
    for i in (",.'?/><}{{}}'@"):
        sentence = sentence.replace(i, "")
    print(sentence)
    palindrome = []
    words = sentence.split(' ')
    print(words)
    for word in words:
        word = word.lower()
        if word == word[::-1]:
            palindrome.append(word)
    return palindrome

sentences = input('Enter a sentence: ')
print(palindrome_words(sentences))
