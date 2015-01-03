import re

dictionary = open("enable2k.txt", "r")

all_words = list([word for line in dictionary for word in line.split()])


def spoonerize(sentence):
    sorted_words = sort_words(sentence)
    spooned_words = check_for_spoons(sorted_words)
    spooned_sentence = replace_with_spoons(spooned_words, sentence)
    spooned_sentence = (" ".join(spooned_sentence))
    spooned_sentence = str.lower(spooned_sentence)
    print(str.capitalize(spooned_sentence))


def sort_words(sentence):
    sentence_words = sentence.split()
    sorted_words = list(enumerate(sentence_words))
    sorted_words.sort(key=lambda t: len(t[1]), reverse=True)
    return sorted_words


def check_for_spoons(sorted_words):
    i = 0
    j = 1
    while i <= (len(sorted_words)-1):
        if j < (len(sorted_words)):
            word1, word2 = list(sorted_words[i]), list(sorted_words[j])
            word1[1], word2[1] = word_swap(sorted_words[i][1], sorted_words[j][1])
            if str.lower(word1[1]) in all_words and str.lower(word2[1]) in all_words:
                return word1, word2
            else:
                j += 1
        else:
            if j >= len(sorted_words):
                if i < (len(sorted_words) - 1):
                    i += 1
                    j = i + 1
    else:
        return 'None'


def word_swap(word1, word2):
    first_vowel1 = re.search("[aeiouy]", word1, re.IGNORECASE)
    first_vowel2 = re.search("[aeiouy]", word2, re.IGNORECASE)
    word2_swapped = word1[0:first_vowel1.start()] + word2[first_vowel2.start():]
    word1_swapped = word2[0:first_vowel2.start()] + word1[first_vowel1.start():]
    return word1_swapped, word2_swapped


def replace_with_spoons(spooned_words, sentence):
    if spooned_words == 'None':
        return "Could not spoonerize the sentence."
    sentence = (list(enumerate(sentence.split())))
    new_sentence = []
    for i in range((len(sentence))):
        spoon_visited_flag = 0
        for j in range((len(spooned_words))):
            if spooned_words[j][0] == sentence[i][0]:
                new_sentence.append(spooned_words[j][1])
                spoon_visited_flag = 1
        else:
            if spoon_visited_flag == 0:
                new_sentence.append(sentence[i][1])
    return new_sentence


user_provided_input = str(input("What sentence would you like to try spoonerizing? "))
spoonerize(user_provided_input)