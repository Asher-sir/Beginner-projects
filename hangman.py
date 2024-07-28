


import random
import string
from words import reserved_words

word =random.choice(reserved_words)
def valid_word(reserved_words):
    while '-' or ' ' in word:
        word=random.choice(reserved_words)
    return word




def hangman ():
    word=valid_word(reserved_words)
    word_letters=set(word)
    alphabets=set(string.ascii_uppercase)
    used_letters=set()

    while len(word_letters)>0:

        print("used letter are  ".join(used_letters))

        word_list=[letter if letter in used_letters else '_' for letter in word]
        print(" current word".join(word_list))




        user_input= input('guess a letter').upper()
        if user_input in alphabets - used_letters:
            used_letters.add(user_input)
            if(user_input in word_letters):
                word_letters.remove(user_input)
        elif(user_input in used_letters):
            print("you have already entered the letter")
        else:
            print("you have not entered a alphabet ")




hangman()





