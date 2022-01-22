import random
# rearrange a list of words

def word_shuffler(word_list):
    og_word_list = word_list.split()
    print(f"the original word list is: {og_word_list}")
    shuffled_word_list = random.sample(og_word_list, len(og_word_list))
    return shuffled_word_list


if __name__ == '__main__':
    word_list = input("type words here separated by space only: ")
    new_sentence = word_shuffler(word_list)
    print(f"you wrote: {word_list}")
    print(f"the rearranged result is: {new_sentence}.")