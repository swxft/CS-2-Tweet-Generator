import sys, random, re

sentence = "one fish two fish red fish blue fish"

words_list = re.split("[\W]+", sentence)

def histogram(source_text, structure = "lol"):
    words_dict = {}

    for word in source_text:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict.update({word: 1}) 

    if structure == "lol":
        print(f"list of lists: {list(map(list, words_dict.items()))}")
    elif structure == "lot" :
        print(f"list of tuples: {list(map(tuple, words_dict.items()))}")
        pass
    return words_dict


if __name__ == '__main__':
    histogram(words_list, "lol")
    histogram(words_list, "lot")
