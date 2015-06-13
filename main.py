
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

def char_counter(file_name):
    input_file = open(file_name, "r")

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

    #for key in letter_list.keys():
        #print("This file contains %s instances of %s" % (letter_list[key], key))

    input_file.close()
    return letter_list


def word_counter(file_name):
    input_file = open(file_name, "r")

    word_list = {}
    for word in input_file.read().split():

        word_stripped = word.strip(",.?!")
        word_lower = word_stripped.lower()

        if word_lower not in word_list:
            word_list[word_lower] = 1
        else:
            word_list[word_lower] += 1

    #for key in word_list.keys():
        #print("This file contains %s instances of %s" % (word_list[key], key))

    input_file.close()
    return word_list


def get_char_percents(_char_nums, num_of_chars):
    char_percent_list = {}
    for letter in ascii_lowercase:
        if letter in _char_nums:
            char_percent = str((float(_char_nums[letter])/num_of_chars)*100)
            char_percent_list[letter] = char_percent
            #print("%s consists of %s percent of input chars" % (str(letter), char_percent))
        else:
            #print("%s consists of 0 percent of input chars" % (str(letter)))
            char_percent_list[letter] = 0

    return char_percent_list


def get_total_chars(_char_nums):
    char_totals = 0
    for items in _char_nums:
        char_totals += _char_nums[items]
    return char_totals


def get_total_words(_word_nums):
    word_total = 0
    for items in _word_nums:
        word_total += _word_nums[items]
    return word_total


if __name__ == '__main__':
    input_file_name = raw_input("Please enter the name of your input .txt file (without extension)\n")
    output_file_name = raw_input("Please enter the name of your output .txt file (without extension)\n")
    extended_input_file_name = input_file_name + ".txt"
    extended_output_file_name = output_file_name + ".txt"

    char_nums = char_counter(extended_input_file_name)
    word_nums = word_counter(extended_input_file_name)

    total_chars = get_total_chars(char_nums)
    total_words = get_total_words(word_nums)
    # time to process the char and word data

    char_percents = get_char_percents(char_nums, total_chars)

    output_file = open(extended_output_file_name, "r+")
    output_file.write("Occurrences of each letter:\n")

    for letter in ascii_lowercase:
        output_file.write("'%s' occurs %s times in the file.  %s percent of total\n" %
                            (letter, char_nums[letter], char_percents[letter]))
    output_file.write("\nTotal number of chars is %s\n" % (total_chars))
    output_file.write("\nWord stats:\n")

    for word in word_nums:
        output_file.write("'%s' occurs %s times\n" % (word, word_nums[word]))
    output_file.write("\nTotal number of words is %s\n" % (total_words))

    sorted_dict = sorted(word_nums.values(), reverse=True)
    top_ten_values = sorted_dict[0:10]
    unique_top_ten_values = list(set(top_ten_values))
    sorted_unique_top_ten_values = sorted(unique_top_ten_values, reverse=True)

    top_word_list = []
    for nums in sorted_unique_top_ten_values:
        for key, value in word_nums.iteritems():
            if value == nums:
                top_word_list.append(key)
        if len(top_word_list) >= 10:
            break

    for ranking in range(1, 11):
        output_file.write("word ranked %s is : %s\n" % (str(ranking), top_word_list[ranking - 1]))
    output_file.close()
