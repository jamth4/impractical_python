''' Decrypt a path through a Union Route Cipher

Designed for whole-world transpostion ciphers with variable rows & columns
Assumes encryption began at either top or bottom of a column
Key indicates the order to read colums and the direction to traverse
Negative column numbers mean start at bottom and read up
Positive column numbres mean start at top and read down.

Example below is for 4x4 matrix with ket -1 2 -3 4.
Note "0" is not allowed
Arrows show encryption route; for negative key values read UP

    1     2     3     4

   ___   ___   ___   ___
  | ^ | | | | | ^ | | | |  MESSAGE IS WRITTEN
  |_|_| |_v_| |_|_| |_v_|
   ___   ___   ___   ___
  | ^ | | | | | ^ | | | |  ACROSS EACH ROW
  |_|_| |_v_| |_|_| |_v_|
   ___   ___   ___   ___
  | ^ | | | | | ^ | | | |  IN THIS MANNER
  |_|_| |_v_| |_|_| |_v_|
   ___   ___   ___   ___
  | ^ | | | | | ^ | | | |  LAST ROW IS FILLED WITH DUMMY WORDS
  |_|_| |_v_| |_|_| |_v_|
  START              END

  Required input - a text message, # of columns, # of rows, key string
  Prints translated plaintext  
'''
import sys

#===============================================================
# USER IMPUT:
# the string to decrypted (typed of paste between triple-quotes):
ciphertext = '''16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19
'''

# number of columns in the transpostion matrix:
COLS = 4

# number of rows in the transpostion matrix:
ROWS = 5

# key with spaces between numbers; negative to read UP columns (ex = -1 2 -3 4)
key = ''' -1 2 -3 4'''

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
 #================================================================

def main():
    """Run program and print decrypted plaintext"""
    print(f'\nCiphertext = {ciphertext}')
    print(f'Trying {COLS} columns')
    print(f'Trying {ROWS} rows')
    print(f'Trying key = {key}')

    # split elements into words, not letters
    cipherlist = list(ciphertext.split())
    validate_col_row(cipherlist)
    key_int = key_to_int(key)
    translation_matrix = build_matrix(key_int, cipherlist)
    plaintext = decrypt(translation_matrix)

    print(f"Plaintext = {plaintext}")

def validate_col_row(cipherlist):
    """Check that input columns & rows are valid vs. message length"""
    factors = []
    len_cipher = len(cipherlist)
    for i in range(2, len_cipher): # ranage excludes 1-column ciphers
        if len_cipher % i == 0:
            factors.append(i)
    print(f'\nLength of cipher = {len_cipher}')
    print(f'Acceptable column/row values include: {factors}')
    print()
    if ROWS * COLS != len_cipher:
        print("\nError - Input columns & rows not factors of length "
              "of cipher. Terminating program.", file=sys.stderr)
        sys.exit()

def key_to_int(key):
    """Turn key into list of integers & check validity"""
    key_int = [int(i) for i in key.split()]
    key_int_lo = min(key_int)
    key_in_hi = max(key_int)
    if len(key_int) != COLS or key_int_lo < -COLS or key_in_hi > COLS \
        or 0 in key_int:
        print("\nError - Problem with key. Terminating.", file=sys.stderr)
        sys.exit(1)
    else:
        return key_int
    
def build_matrix(key_int, cipherlist):
    """Turn every n items in a list into a new item in a list of lists"""
    translation_matrix = [None] * COLS
    start = 0
    stop = ROWS
    for k in key_int:
        if k < 0: # read bottom-to-top of column
            col_items = cipherlist[start:stop]
        elif k > 0: # read top-to-bottom of column
            col_items = list((reversed(cipherlist[start:stop])))
        translation_matrix[abs(k) - 1] = col_items
        start += ROWS
        stop += ROWS
    return translation_matrix

def decrypt(translation_matrix):
    """Loop through nested lists popping off last item to a string."""
    plaintext = ''
    for i in range(ROWS):
        for matrix_col in translation_matrix:
            word = str(matrix_col.pop())
            plaintext += word + ' '
    return plaintext

if __name__ == '__main__':
    main()