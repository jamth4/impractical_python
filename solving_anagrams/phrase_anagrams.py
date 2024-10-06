import sys
from collections import Counter
import load_dictionary

dict_file = load_dictionary.load('solving_anagrams//words.txt')
# ensure "a" and "I" (both lowercase) are included
dict_file.append("a")
dict_file.append("I")
dict_file = sorted(dict_file)

ini_name = input("Enter a name:")

def find_anagrams(name, word_list):
    """Read name and dictionary file and display all anagrams
    in name"""

    name_letter_map = Counter(name)
    anagrams = []
    for word in word_list:
        test = ''
        word_letter_map = Counter(word.lower())
        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
        if Counter(test) == word_letter_map:
            anagrams.append(word)
    print(*anagrams, sep='\n')
    print()
    print(f'Remaining letter {name}')
    print(f'Number of remaining leters {len(name)}')
    print(f'Number of remaining (real word) anagrams = {len(anagrams)}')

def process_choice(name):
    """Check user choice for validity, return choice and left over letters."""

    while True:
        choice = input('\nMake a choice else Enter to start over or # to end: ')
        if choice == '':
            main()
        elif choice == '#':
            sys.exit()
        else:
            candidate = ''.join(choice.lower().split())
        left_over_list = list(name)
        for letter in candidate:
            if letter in left_over_list:
                left_over_list.remove(letter)
        if len(name) - len(left_over_list) == len(candidate):
            break
        else:
            print("Won't work! Make another choice!", file=sys.stderr)
    name = ''.join(left_over_list) # makes display more readable
    return choice, name

def main():
    '''Help user build anagram phrase from their name'''
    name = ''.join(ini_name.lower().split())
    name = name.replace('-', '')
    limit = len(name)
    phrase = ''
    running = True

    while running:
        temp_phrase = phrase.replace(' ', '')
        if len(temp_phrase) < limit:
            print(f'Length of anagram phrase = {temp_phrase}')
            find_anagrams(name, dict_file)
            print('Current anagram phrase =', end=" ")
            print(phrase, file=sys.stderr)

            choice, name = process_choice(name)
            phrase += choice + ' '

        elif len(temp_phrase) == limit:
            print("\n*****FINISHED!!!*****\n")
            print("Anagrams of name =", end=" ")
            print(phrase, file=sys.stderr)
            print()
            try_again = input('\nTry again? (Press Enter else "n" to quit)\n')
            if try_again.lower() == "n":
                running = False
                sys.exit()
            else:
                main()

if __name__ == '__main__':
    main()
