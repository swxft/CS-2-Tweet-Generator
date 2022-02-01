import sys, random, text_analysis, sample
#  generate sentences from a body of text.

def random_python_quote(corpus, words_requested):
    with open(corpus) as vocabulary:
        text_body = vocabulary.read().split()
        new_words = (random.choices(text_body, k = int(words_requested)))
        new_sentence = " ".join(new_words)
        # print(f"{new_sentence}.")
    return new_sentence

def histogram_random_word(histogram_tuple_list, words_requested = 1):
    key_list = []
    for pair in histogram_tuple_list:
        key_list.append(pair) # windmill
    # print(f"key list: {key_list}")
    new_words = (random.choices(key_list, k = int(words_requested)))
    new_sentence = " ".join(new_words)
    return new_sentence

def stochastic_random(histogram_tuple_list, words_requested = 1):
    key_list = []
    for pair in histogram_tuple_list:
        key_list.append(pair) # windmill
        print(f"pair: {pair}")
        print(f"pair: {pair[0]}")
        # print(f"key list: {key_list}")
    # new_words = (random.choices(key_list, k = int(words_requested)))
    # new_sentence = " ".join(new_words)
    # return new_sentence
    pass

def uniform_list(histogram_tuple_list, words_requested = 1):
    # print(histogram_tuple_list)
    token_list = []
    for pair in histogram_tuple_list:
        type, token = pair[0], pair[1]
        token_list.extend([type] * token)
    # print(len(token_list))
    return token_list

if __name__ == '__main__':
    # corpus_location word_amount
    list_user_args = sys.argv[1:] #list
    # words_requested = " ".join(list_user_args[1])
    # random_python_quote(list_user_args[0], words_requested)
    histogram_tuple_list = text_analysis.histogram(list_user_args[0])
    # print(sample.number_line(histogram_tuple_list))
    print(f" list: {uniform_list(histogram_tuple_list)}")
    