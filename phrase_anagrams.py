import load_dictionary
from collections import Counter
import pprint

oxford_dict_words = load_dictionary.load("/Users/umarpatel/Desktop/Text Files For Coding Practice/dictionary.txt")

def is_word_anagram(_word, _phrase_chars):
    _word = _word.lower()
    _word_count = Counter(_word)
    for character in _word_count:
        if character not in _phrase_chars:
            return False
        if _word_count[character] > _phrase_chars[character]:
            return False
    return True

def find_word_anagrams(oxford_words, phrase_chars):
    list_of_possible_anagrams = []
    for word in oxford_words:
        if is_word_anagram(word, phrase_chars):
            list_of_possible_anagrams.append(word)
    return list_of_possible_anagrams


phrase = input("Enter a phrase you'd like to find anagram phrases for:\n")
phrase = phrase.replace(" ", '')
phrase = phrase.lower()
phrase_chars_count = Counter(phrase)
anagram_phrase = ""

while len(phrase_chars_count) != 0:
    print("These are your options:\n")
    word_options = find_word_anagrams(oxford_dict_words, phrase_chars_count)
    if len(word_options) == 0:
        user_input = input("There are no word options. \"t\" to try again or \"q\" to quit\n")
        if user_input == 't':
            phrase_chars_count = Counter(phrase)
        else:
            print("the program has finished")
            break
    else:
        pprint.pprint(word_options)
        print("\nThis is your current phrase: " + anagram_phrase + "\n")
        chars_left = 0
        for key in phrase_chars_count:
            chars_left += phrase_chars_count[key]
        print("You have " + str(chars_left) + " characters left to use\n")
        choice = input("Choose one of the above words. Enter \"start over\" to start over or \"q\" to quit:\n")
        if choice == "start over":
            phrase_chars_count = Counter(phrase)
        elif choice == 'q':
            print("the program has finished")
            break
        else:
            while choice not in word_options:
                print("Sorry, that doesn't seem to be an option. Please try to choose a word from the list:\n")
                pprint.pprint(word_options)
                choice = input("Choose one of the above words:\n")
            for char in choice:
                phrase_chars_count[char] = phrase_chars_count[char] - 1
                if phrase_chars_count[char] == 0:
                    phrase_chars_count.pop(char)

            if len(phrase_chars_count) == 0:
                anagram_phrase = anagram_phrase + choice
            else:
                anagram_phrase = anagram_phrase + choice + " "

if len(phrase_chars_count) == 0:
    print("Here is your anagram phrase:")
    print(anagram_phrase)