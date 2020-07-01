import numpy as np
from collections import defaultdict
import pprint

coded_message = input("Enter the coded message:\n")
coded_message_words = coded_message.split()
for i in range(len(coded_message_words)):
    coded_message_words[i] = coded_message_words[i].lower()

code_words = defaultdict(str)
possible_code_words = []
for i in range(len(coded_message_words)):
    possible_code_words.append(coded_message_words[i])

pprint.pprint(possible_code_words)
word_in_coded_message = input("Enter a word in the coded message from above that is a code word. Enter 's' to stop if there are none:\n")
while len(possible_code_words) != 0 and word_in_coded_message != 's':
    if word_in_coded_message.lower() in possible_code_words:
        substitute_word = input("What word takes the place of this?\n")
        code_words[word_in_coded_message.lower()] = substitute_word
        i = 0
        while i != len(possible_code_words):
            if possible_code_words[i] == word_in_coded_message.lower():
                possible_code_words.pop(i)
            else:
                i += 1
    else:
        print("Sorry, the word " + word_in_coded_message + " is not in the coded message.\n")
        pprint.pprint(possible_code_words)
        word_in_coded_message = input("Enter a word in the coded message from above that is a code \nword. Enter 's' to stop if there are none:\n")

    if len(possible_code_words) == 0:
        print("All words have a code word to them.\n")

num_rows = int(input("Enter the number of rows:\n"))
num_cols = int(input("Enter the number of columns:\n"))

while num_rows * num_cols < len(coded_message):
    print("You're inputs for rows and columns do not provide enough space for the coded message.\n")
    print("Please enter a valid number of rows and columns:\n")
    num_rows = input("Enter number of rows:\n")
    num_cols = input("Enter number of columns:\n")

keys = input("Enter key:\n")
keys = keys.split()
while len(keys) != num_cols:
    print("Sorry, you have too many or to few directional keys in your key list. Please try again:\n")
    keys = input("Enter the key:\n")
    keys = keys.split()
keys = [int(x) for x in keys]

print("You will now enter the filler words in their respective order.\nIf they repeat, only print out one cycle of the filler words.\n")
filler_words = []
num = 1
pprint.pprint(possible_code_words)
word = input("Enter filler word from above. This will be filler word number " + num + ". Enter 's' to stop")
while len(possible_code_words) != 0 or word != 's':
    if word in possible_code_words:
        filler_words.append(word)
        j = 0
        while j < len(possible_code_words):
            if possible_code_words[j] == word:
                possible_code_words.pop(j)
            else:
                j += 1
        num += 1
    else:
        print("Sorry, it doesn't look like " + word + " is available in the message to be a filler word. Try again:\n")

    if len(possible_code_words == 0):
        break
    else:
        pprint.pprint(possible_code_words)
        word = input("Enter filler word from above. This will be filler word number " + num + ". Enter 's' to stop")

if len(possible_code_words == 0):
    print("There are no more words available to be filler words.\n")

def decode_route_cipher(message_words, codewords, filler_word_list, rows, cols, key):
    matrix = np.zeros(shape=(rows, cols), dtype=object)
    for c in range(cols):
        col_list = []
        for w in range(rows):
            col_list.append(message_words.pop(0))
        if abs(key[c]) < 0:
            col_list.reverse()
        matrix[:, abs(key[c]) - 1] = col_list

    unscrambled_words_list = []
    for r in range(rows):
        for c in range(cols):
            unscrambled_words_list.append(matrix[r, c])

    curr_index = 0
    while curr_index < len(unscrambled_words_list):
        

