import random, sys
# rearrange a list of words

def word_shuffler(word_input):
    shuffled_words = tuple(random.sample(word_input, len(word_input)))
    return shuffled_words


if __name__ == '__main__':
    word_input = sys.argv[1:]
    new_sentence = " ".join(word_shuffler(word_input))
    print(f"the rearranged result is: {new_sentence}.")