import load_dictionary
import time

word_list = load_dictionary.load('finding_palingram_spells//words.txt')
words = set(word_list)

# find word-pair palingrams

def find_palingrams():
    '''Find dicitonary palingrams'''
    pali_list = []

    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in words:
                    pali_list.append((rev_word[:end-i], word))
    return pali_list
start_time = time.time()
palingrams = find_palingrams()
end_time = time.time()
# sort palingrams on first word
palingrams_sorted = sorted(palingrams)

#display list of palingrams

print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print("{} {}".format(first, second))

print("Runtime for this program was {} seconds.".format(end_time - start_time))