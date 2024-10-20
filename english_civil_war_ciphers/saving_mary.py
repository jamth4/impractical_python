import load_dictionary
import string
from random import randint

init_message = 'Give your word and we rise'
message = ''

for char in init_message:
    if char in string.ascii_letters:
        message += char

print(message)

supporters = load_dictionary.load('english_civil_war_ciphers//supporters.txt')

supporter_list = []
supporter_list.append(supporters[0])


counter = 1
for letter in message:
    for word in supporters:       
        if len(word) > 2 and word not in supporter_list: 
            if counter % 2 == 0 and word[2].lower() == letter.lower():
                # print(word, 'if')
                supporter_list.append(word)
                counter += 1
                break
            elif counter % 2 != 0 and word[1].lower() == letter.lower():
                # print(word, 'elif')
                supporter_list.append(word)
                counter += 1
                break

supporter_list.insert(3, 'John')
supporter_list.insert(6, 'Bill')

print('Supporter list for message is: ', *supporter_list, sep='\n')