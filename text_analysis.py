import sys, random, dictionary_words, timeit
# categorize tokens by their types
def histogram(source_location, structure = "lot"):
    with open(source_location) as lrg_string:
        words_list = lrg_string.read().split()
        words_dict = {}

    for word in words_list:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict.update({word: 1}) 

    if structure == "lol":
        # print(f"dictionary: {words_dict.items()}")
        words_dict = list(map(list, words_dict.items()))
    elif structure == "lot":
        words_dict = list(map(tuple, words_dict.items()))
    return words_dict

def unique_words(histogram_tuple):
    # when given the histogram for The Adventures of Sherlock Holmes, it returns the integer 8475.
    unique_words = len(histogram_tuple)
    return unique_words

def frequency(histogram_tuple_list, word = "you"):
    # For example, when given the word "mystery" and the Holmes histogram, it will return the integer 20.
    key_list = []
    for pair in histogram_tuple_list:
        key_list.append(pair[0]) # windmill
    tuple_index = key_list.index(word)  #21
    tuple_item = histogram_tuple_list[tuple_index]
    word_frequency = tuple_item[-1] # 4
    return word_frequency


if __name__ == '__main__':

    # python3 text_analysis.py text_file structure frequency
    # "lot" list of tuples and "lol" list of lists
    list_user_args = sys.argv[1:] # list of args starting with the 2nd item

    # test the histogram function
    histogram(list_user_args[0], list_user_args[1])

    # test result
    histogram_result = histogram(list_user_args[0])

    # test unique words
    print(f"the amount of unique words is: {unique_words(histogram_result)}")

    # test frequency of words
    # print(f"frequency of your word is: {frequency(histogram_result, 'windmill')}")
    print(f"frequency of your word is: {frequency(histogram_result, list_user_args[-1])}")

    # list_test = timeit.timeit(histogram("feels_good_inc.txt", "lot"), number=1000000)