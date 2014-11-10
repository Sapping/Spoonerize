dictionary = open("dictionary.txt", "r")

output = open("spoons.txt", "w")

all_words = set([word.split()[0] for word in dictionary])

def firstletter_swap(word, companion):
    word_spoon = companion[0] + word[1:]
    companion_spoon = word[0] + companion[1:]
    return word_spoon, companion_spoon

