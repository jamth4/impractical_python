
# Load the ciphertext string.
ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"
# Convert ciphertext into a cipherlist to split out individual words.
cipherlist = list(ciphertext.split())


# Get input for the number of columns and rows.
# Get input for the key.
COLS = 4
ROWS = 5
key = '-1 2 -3 4' # negative number means read UP column vs. DOWN
translation_matrix = [None] * COLS
plaintext = ''
start = 0
stop = ROWS
# Convert key into a list to split out individual numbers.
key_int = [int(i) for i in key.split()]


# turn columns into items in list of lists
for k in key_int:
    if k < 0: # reading bottom-to-top of column
        col_items = cipherlist[start:stop]
    elif k > 0: # reading top-to-bottom of column
        col_items = list((reversed(cipherlist[start:stop])))
    translation_matrix[abs(k) - 1] = col_items
    start += ROWS
    stop += ROWS

print(f'\nchipertext = {ciphertext}')
print('\ntranslation matrix =', *translation_matrix, sep="\n")
print(f'\nkeylength = {len(key_int)}')

# loop through nested list popping off last item to new list:
for i in range(ROWS):
    for col_items in translation_matrix:
        word = str(col_items.pop())
        plaintext += word + ' '

print(f'\nplaintext = {plaintext}')
