
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

if __name__ == '__main__':
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

    for key in letter_list.keys():
        print("This file contains %s instances of %s" %(letter_list[key], key))

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
    #print(word)



    #print(words)
