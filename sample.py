# import re, random
import sys, random, text_analysis, dictionary_words
# from threading import get_ident

def random_word_from_histogram(file, words_requested):
    histogram = text_analysis.histogram(file, words_requested) #list of tuples
    word = dictionary_words.histogram_random_word(histogram)
    return(word)

def random_word_from_file(file, words_requested = 1):
    word = dictionary_words.random_python_quote(file, words_requested)
    return(word)

def sample_word(histogram_tuple_list, unique_words):
    print(f"type list: {histogram_tuple_list}")
    distance = 0
    dart = random.randint(1, len(unique_words) -1)
    print(f"dart: {dart}"), print(f"tokens: {len(unique_words)}")
    for word in histogram_tuple_list:
        print(f"word: {word}")
        type, token = word[0], word[1]
        distance += token
        print(f"DISTANCE is: {distance}")
        if distance >= dart:
            random_word = type
            break
        else:
            pass
    return random_word

def number_line(histogram_tuple):
    token_list = []
    for pair in histogram_tuple:
        type, token = pair[0], pair[1]
        token_list.extend([type] * token)
    return token_list

if __name__ == '__main__':
    list_user_args = sys.argv[1:] #list

    hish = text_analysis.histogram("onefish.txt")
    # print(number_line(hish))
    sample_word(hish, dictionary_words.uniform_list(text_analysis.histogram("onefish.txt")))
    # dictionary_words.random_python_quote(list_user_args[0], words_requested[1])
