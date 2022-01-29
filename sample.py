import sys, random, text_analysis, dictionary_words

def random_word_from_histogram(file, words_requested):
    histogram = text_analysis.histogram(file, words_requested) #list of tuples
    word = dictionary_words.histogram_random_word(histogram)
    return(word)

def random_word_from_file(file, words_requested = 1):
    word = dictionary_words.random_python_quote(file, words_requested)
    return(word)


if __name__ == '__main__':
    list_user_args = sys.argv[1:] #list
    # words_requested = " ".join(list_user_args[-1])
    # corpus_location word_amount
    print(f"word from histogram: {random_word_from_histogram(list_user_args[0],1)}")
    # corpus_location word_amount
    print(f"word from file: {random_word_from_file(list_user_args[0],1)}")
    # dictionary_words.random_python_quote(list_user_args[0], words_requested[1])
