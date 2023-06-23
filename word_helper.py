import random

def pick_word(length=5):

    with open('words_alpha.txt', 'r') as f: #https://github.com/dwyl/english-words
        wordlist = f.read().strip('\n').split('\n')
    word = ''
    while len(word) != length:
        word = random.choice(wordlist)
    print(word)
    return word

def check_word(word):
    with open('words_alpha.txt', 'r') as f: #https://github.com/dwyl/english-words
        wordlist = f.read().strip('\n').split('\n')
    return True if word in wordlist else False