import sys, random, re

def histogram(source_location, structure = "lol"):
    with open(source_location) as lrg_string:
        words_list = lrg_string.read().split()
        words_dict = {}

    for word in words_list:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict.update({word: 1}) 

    if structure == "lol":
        print(f"list of lists: {list(map(list, words_dict.items()))}")
    elif structure == "lot" :
        print(f"list of tuples: {list(map(tuple, words_dict.items()))}")
    return words_dict


if __name__ == '__main__':
    histogram("feels_good_inc.txt", "lol") # list of lists
    histogram("feels_good_inc.txt", "lot") # list of tuples
