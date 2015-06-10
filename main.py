
# Write a Python program that reads a text file and reports statistics on the file.
# The statistics are as follows:
#  The number of occurrences of each letter in in the alphabet (regardless of case). The
# frequency should also be reported as a percentage of each letter over all the non-
# whitespace characters in the text file (including numbers and punctuation) . Note that the
# reporting for each letter is not case sensitive.
#  The ten most frequently occurring words in the text file.
#  The number of words in the text file.
#  The number of non-whitespace characters in the text file.

from string import punctuation
from string import ascii_lowercase

def char_counter():
    input_file = open("input_file.txt", "r")

    punct = set(punctuation)
    punct.add("\n")
    punct.add(" ")
    letter_list = {}
    for letter in input_file.read():
        if letter in punct:
            continue
        letter_lower = letter.lower()

        if letter_lower not in letter_list:
            letter_list[letter_lower] = 1
        else:
            letter_list[letter_lower] += 1

    for letter in ascii_lowercase:
            if letter not in letter_list:
                letter_list[letter] = 0

    for key in letter_list.keys():
        print("This file contains %s instances of %s" %(letter_list[key], key))

    input_file.close()
    return letter_list


def word_counter():
    input_file = open("input_file.txt", "r")

    word_list = {}
    for word in input_file.read().split():

        word_stripped = word.strip(",.?!")
        word_lower = word_stripped.lower()

        if word_lower not in word_list:
            word_list[word_lower] = 1
        else:
            word_list[word_lower] += 1

    for key in word_list.keys():
        print("This file contains %s instances of %s" %(word_list[key], key))

    input_file.close()
    return word_list

def get_char_percents(input_data):
    num_of_chars = get_total_chars(input_data)
    char_percent_list = {}
    for letter in ascii_lowercase:
        if letter in char_analysis:
            char_percent = str((float(char_analysis[letter])/num_of_chars)*100)
            char_percent_list[letter] = char_percent
            print("%s consists of %s percent of input chars" %(str(letter), char_percent))
        else:
            print("%s consists of 0 percent of input chars" %(str(letter)))
            char_analysis[letter] = 0


def get_total_chars(input_data):
    char_totals = 0
    for items in char_analysis:
        char_totals += char_analysis[items]
    return char_totals


def get_total_words(input_data):
    word_total = 0
    for items in word_analysis:
        word_total += word_analysis[items]
    return word_total


if __name__ == '__main__':
    # get file input and output name
    input_file_name = raw_input("Please enter the name of your input .txt file (without extension)\n")
    output_file_name = raw_input("Please enter the name of your output .txt file (without extension)\n")

    extended_input_file_name = input_file_name + ".txt"
    extended_output_file_name = output_file_name + ".txt"

    char_analysis = char_counter()
    word_analysis = word_counter()

    # time to process the char and word data

    char_percents = get_char_percents(char_analysis)

    output_file = open(extended_output_file_name, "w")

    num_of_words = get_total_words(word_analysis)
