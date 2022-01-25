from hashlib import new
import sys, random, re
#  generating sentences from a body of text in a text file. 

def random_python_quote(corpus, words_requested):
    with open(corpus) as dictionary:
        text_body = dictionary.read().splitlines()
        new_words = (random.choices(text_body, k = int(words_requested)))
        new_sentence = " ".join(new_words)
        print(f"{new_sentence}.")
    return new_sentence

if __name__ == '__main__':
    # corpus_location word_amount
    list_user_args = sys.argv[1:] #list
    words_requested = " ".join(list_user_args)
    random_python_quote('words.txt', words_requested)
    