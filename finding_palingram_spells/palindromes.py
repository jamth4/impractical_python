#Pseudocode
#Load digital dictionary file as list of words
#Loop through each word in the word list
#   IF a word sliced forward is the same as the word sliced backward:
#       Append word to palindrom list
#Print palindrome list

"""
Find palindromes (letter palingrams) in a dictionary file
"""

import load_dictionary
word_list = load_dictionary.load('finding_palingram_spells//words.txt')

pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print("\nNumber of palindromes found = {}\n".format(len(pali_list)))

print(*pali_list, sep='\n')