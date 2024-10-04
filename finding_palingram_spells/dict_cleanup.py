import load_dictionary

word_list = load_dictionary.load('finding_palingram_spells//word2.txt')

for word in word_list:
    if len(word) <= 1:
        print(word)
        word_list.remove(word)