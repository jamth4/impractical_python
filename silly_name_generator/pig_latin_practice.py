"""Converts input to pig latin"""

def main():
    """Takes word input and converts to pig latin"""
    word =input('Enter a word to convert to pig latin:\n')

    vowels = ("a", "e", "i", "o", "u", "y")

    if word[0] in vowels:
        new_word = word + 'way'

    else:
        ending = word[0] + 'ay'
        new_word = word[1:] + ending
    
    print(new_word)


if __name__ == "__main__":
    main()
