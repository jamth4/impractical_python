"""
Load a text file as a list
Arugument:
-text file name (and directory path, if needed)

Exceptions:
-IOError is filename not found

Returns:
-A list of all words in a text file in lower case.
"""
import sys

def load(file):
    """Open a file and return a list of lowercase strings"""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program".format(e, file),
              file=sys.stderr)
        sys.exit(1)
    