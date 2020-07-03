import pprint
import numpy as np
from collections import defaultdict

original_text = input("Enter text:\n")
cipher_list = original_text.split()
for i in range(len(cipher_list)):
    cipher_list[i] = cipher_list[i].lower()

words = []
for i in range(len(cipher_list)):
    words.append(cipher_list[i])

num_rows = int(input("Enter number of rows:\n"))
num_cols = int(input("Enter number of columns:\n"))

while num_rows * num_cols < len(cipher_list):
    print("You're inputs for rows and columns do not provide enough space for the ciphertext.\n")
    print("Please enter a valid number of rows and columns:\n")
    num_rows = input("Enter number of rows:\n")
    num_cols = input("Enter number of columns:\n")

key = input("Enter the key:\n")
key_list = key.split()
while len(key_list) != num_cols:
    print("Sorry, you have too many or to few directional keys in your key list. Please try again:\n")
    key = input("Enter the key:\n")
    key_list = key.split()
key_list = [int(x) for x in key_list]

possible_words = []
for word in cipher_list:
    possible_words.append(word)

code_words = defaultdict(str)
print("You are now going to create code words:\n")
pprint.pprint(possible_words)
word = input("Enter a word from above. Type \'s\' to stop:\n")
code_for_word = ""
while word != 's':
    if word.lower() in cipher_list:
        code_for_word = input("What is the code word for " + word.lower() + "?\n")
        for k in range(len(cipher_list)):
            if cipher_list[k] == word.lower():
                cipher_list[k] = code_for_word
        code_words[word.lower()] = code_for_word
        i = 0
        while i != len(possible_words):
            if possible_words[i] == word.lower():
                possible_words.pop(i)
            else:
                i += 1
    else:
        print("Sorry, " + word.lower() + " is not a word in the text to be encoded or it already has a code word.\n")

    pprint.pprint(possible_words)
    word = input("Enter a word from above. Type \'s\' to stop:\n")
    if len(possible_words) == 0:
        print("There are no more words left to make code words for\n")
        break

print("\nThese are the code words:\n")
print(code_words)
print("\n")

transposition_matrix = []

for i in range(num_cols):
    col = []
    for k in range(num_rows):
        if len(cipher_list) > i + (k * num_cols):
            col.append(cipher_list[i + (k * num_cols)])
        if len(cipher_list) <= i + (k * num_cols) or k == num_rows - 1:
            transposition_matrix.append(col)
            break

translation_matrix = []

for j in range(num_cols):
    a = transposition_matrix[abs(key_list[j]) - 1]
    translation_matrix.append(a)

first_smallest_column_index = 0
for c in range(num_cols):
    if len(translation_matrix[c]) < len(translation_matrix[first_smallest_column_index]):
        first_smallest_column_index = c
        break

# you can change filler word list to whatever you please. Ensure words in filler_words list
# are not actual words in the real message to prevent confusion.
filler_words = []
for key in code_words:
    words.append(code_words[key])
num = 1
pprint.pprint(words)
f_w = input("\nEnter filler word number " + str(num) + ". Make sure they are not any of \nthe words above to avoid confusion. Only enter words that make up \none cycle if they will repeat. Enter 's' to stop.\n")
while f_w != 's':
    if f_w not in words and f_w not in filler_words:
        filler_words.append(f_w)
        num += 1
    else:
        print("\nSorry, it looks like your filler word cannot be used. Please try to make it unique.\n")

    pprint.pprint(words)
    f_w = input("\nEnter filler word number " + str(num) + ". Make sure they are not any of \nthe words above to avoid confusion. Only enter words that make up \none cycle if they will repeat. Enter 's' to stop.\n")



curr_filler_index = 0
curr_col_index = first_smallest_column_index
while len(translation_matrix[curr_col_index]) < num_rows:
    translation_matrix[curr_col_index].append(filler_words[curr_filler_index])
    if curr_col_index == num_cols - 1:
        curr_col_index = 0
    else:
        curr_col_index += 1
    if curr_filler_index == len(filler_words) - 1:
        curr_filler_index = 0
    else:
        curr_filler_index += 1

route_cipher_encoding = np.zeros(shape=(num_rows, num_cols), dtype=object)
for col in range(num_cols):
    route_cipher_encoding[:, col] = translation_matrix[col]

cyphertext = ""
curr_col = []
for l in range(num_cols):
    if key_list[l] < 0:
        curr_col = route_cipher_encoding[:, abs(key_list[l]) - 1][::-1]
    else:
        curr_col = route_cipher_encoding[:, abs(key_list[l]) - 1]
    for i in range(num_rows):
        if l == num_cols - 1 and i == num_rows - 1:
            cyphertext += curr_col[i]
        else:
            cyphertext += curr_col[i] + " "

print("This is the direction key:\n")
print(key + "\n")
print("This is the translation matrix:\n")
pprint.pprint(translation_matrix)
print("\n")
print("This is the code word chart:\n")
print(route_cipher_encoding)
print("\n")
print("This is the encoded text:\n")
print(cyphertext)