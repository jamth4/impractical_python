"""
To Do:
Load digital dictionary file as a list of words
Accept a word from user
create an empty list to hold anagrams
sort the user word
loop through each word in the word list:
    sort the word
    if word sorted is equal to user-word sorted:
        append word to anagrams list
Print anagrams list
"""
import load_dictionary
word_list = load_dictionary.load('solving_anagrams//words.txt')

anagrams_list = []

#input a single word or single name below to find its anagram
name = 'foster'
print(f"Input name = {name}")

name = name.lower()
print(f"Using name = {name}")

# sort name & find anagrams

name_sorted = sorted(name)
for word in word_list:
    word = word.lower()
    if word != name:
        if sorted(word) == name_sorted:
            anagrams_list.append(word)
#print out list of anagrams
print()

if len(anagrams_list) == 0:
    print('You need a larger dictionary or a new name')
else:
    print("Anagrams =", *anagrams_list, sep='\n')