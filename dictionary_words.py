import sys, random, re
#  generate sentences from a body of text in a file. 

def random_python_quote(corpus, words_requested):
    with open(corpus) as vocabulary:
        text_body = vocabulary.read().split()
        new_words = (random.choices(text_body, k = int(words_requested)))
        new_sentence = " ".join(new_words)
        print(f"{new_sentence}.")
    return new_sentence

if __name__ == '__main__':
    # corpus_location word_amount
    list_user_args = sys.argv[1:] #list
    words_requested = " ".join(list_user_args[1])
    random_python_quote(list_user_args[0], words_requested)
    