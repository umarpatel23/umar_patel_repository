plaintext = input("Enter phrase:\n")
text = plaintext.upper();
text = text.replace(" ", "")

top_string = ""
bottom_string = ""
for i in range(len(text)):
    if i % 2 == 0:
        top_string += text[i]
    else:
        bottom_string += text[i]

merged_strings = top_string + bottom_string

chars_per_word = input("\nThere are " + str(len(merged_strings)) + " chars in the coded text.\nHow many characters do you want per word\nin the encoded text? Note that the last word\nmay have less characters than this value.\n")
chars_per_word = int(chars_per_word)
encoded_message = ""
curr_word = ""
j = 0

while j < chars_per_word and len(merged_strings) != 0:
    curr_word += merged_strings[0]
    merged_strings = merged_strings.replace(merged_strings[0], "", 1)

    if len(merged_strings) == 0:
        encoded_message += curr_word
        break

    if j == chars_per_word - 1:
        encoded_message += curr_word + " "
        curr_word = ""
        j = 0
    else:
        j += 1

print("\nHere is your encoded message:\n")
print(encoded_message)