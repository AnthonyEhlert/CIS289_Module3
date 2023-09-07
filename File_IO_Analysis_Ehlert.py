"""
Program Name: File_IO_Analysis_Ehlert.py
Author: Tony Ehlert
Date: 9/6/2023

Program Description: This program reads two different text files and manipulates the text from the files so it can
be used for analysis
"""
import re

def read_text_file_to_dict(text_file):
    """
    The function accepts a text file and then reads it as an input file and creates a dictionary of each word(key)
    contained in the file, along with the number of times(value) each word was used and returns the dictionaru
    :param text_file: file to be read
    :return: dictionary with keys being the words used, and values being the number of times the key/word was used
    """
    # create empty dictionary to sore words from file
    word_count_dict = {}

    # read the text file
    with open(text_file, 'r') as input_file:
        for line in input_file:
            # convert all characters in line to lowercase
            line = line.lower()
            # remove any punctuation
            cleaned_line = re.sub(r'[^\w\s]', '', line)
            # split the line into words
            split_line = cleaned_line.split()

            # add the words from the line to a dictionary
            for word in split_line:
                # check if word already exists as key in dictionary
                if word in word_count_dict.keys():
                    # word/key was already in dict, thus count/value for key increased by one
                    word_count_dict[word] += 1
                else:
                    # word/key not in dict, thus word/key added to dict with a count of one
                    word_count_dict[word] = 1

    # return completed word count dictionary
    return word_count_dict

if __name__ == "__main__":
    # call function to create and get dictionary of word count for Moby_Dick_Chapter_1.txt
    moby_dick_word_dict = read_text_file_to_dict('Moby_Dick_Chapter_1.txt')

    # sort the dictionary and store in new variable
    sorted_moby_dick_word_dict = sorted(moby_dick_word_dict.items(), key=lambda x: x[1], reverse=True)
    #print(sorted_moby_dick_word_dict)

    # Determine how many times the word "old" appears in the passage
    if 'old' in moby_dick_word_dict.keys():
        print(f"The word \"old\" appears in \"Moby_Dick_Chapter_1.txt\" {moby_dick_word_dict['old']} times.")
    else:
        print(f"The word \"old\" does not appear in \"Moby_Dick_Chapter_1.txt\".")

    # Determine how many times the word "water" appears in the passage
    if 'water' in moby_dick_word_dict.keys():
        print(f"The word \"water\" appears in \"Moby_Dick_Chapter_1.txt\" {moby_dick_word_dict['water']} times.")
    else:
        print(f"The word \"water\" does not appear in \"Moby_Dick_Chapter_1.txt\".")

    # Determine the average sentence length in the passage (splitting on periods will suffice)
    sentences = []
    total_text = ''
    with open('Moby_Dick_Chapter_1.txt', 'r') as text_file:
        # split the text_file into list of sentences
        for line in text_file:
            total_text += line
    sentences = total_text.split('.')

    # set number of sentences in Moby_Dick_Chapter_1 and check for emtpy string as last value in sentences list.
    num_of_sentences = 0
    if sentences[-1] == '':
        num_of_sentences = len(sentences) - 1
    else:
        num_of_sentences = len(sentences)
    print(f"{num_of_sentences} sentences in \"Moby_Dick_Chapter_1.txt\"")

    # set number of words in Moby_Dick_Chapter_1
    num_of_words = sum(moby_dick_word_dict.values())
    print(f"{sum(moby_dick_word_dict.values())} words in \"Moby_Dick_Chapter_1.txt\"")

    # print the average sentence length to the console
    print(f"The average length of sentence in \"Moby_Dick_Chapter_1.txt\" is {num_of_words/num_of_sentences:.2f} words")

    # print new line to separate printouts of dictionaries
    print()

    # Do the same things as with chapter 1 in Sense_and_Sensibility_Chapter_1.txt
    # call function to create and get dictionary of word count for Sense_and_Sensibility_Chapter_1.txt
    s_and_s_word_dict = read_text_file_to_dict('Sense_and_Sensibility_Chapter_1.txt')

    # sort the dictionary and store in new variable
    sorted_s_and_s_word_dict = sorted(s_and_s_word_dict.items(), key=lambda x:x[1], reverse=True)
    #print(sorted_s_and_s_word_dict)

    # Determine how many times the word "old" appears in the passage
    if 'old' in s_and_s_word_dict.keys():
        print(f"The word \"old\" appears in \"Sense_and_Sensibility_Chapter_1.txt\" {s_and_s_word_dict['old']} times.")
    else:
        print(
            f"The word \"old\" does not appear in \"Sense_and_Sensibility_Chapter_1.txt\"")

    # Determine how many times the word "water" appears in the passage
    if 'water' in s_and_s_word_dict.keys():
        print(f"The word \"water\" appears in \"Sense_and_Sensibility_Chapter_1.txt\" {s_and_s_word_dict['water']} times.")
    else:
        print(
            f"The word \"water\" does not appear in \"Sense_and_Sensibility_Chapter_1.txt\"")

    # Determine the average sentence length in the passage (splitting on periods will suffice)
    sentences = []
    total_text = ''
    with open('Sense_and_Sensibility_Chapter_1.txt', 'r') as text_file:
        # split the text_file into list of sentences
        for line in text_file:
            total_text += line
    sentences = total_text.split('.')

    # set number of sentences and check for emtpy string as last value in sentences list.
    num_of_sentences = 0
    if sentences[-1] == '':
        num_of_sentences = len(sentences)-1
    else:
        num_of_sentences = len(sentences)
    print(f"{num_of_sentences} sentences in \"Sense_and_Sensibility_Chapter_1.txt\"")

    # set number of words in Sense_and_Sensibility_Chapter_1
    num_of_words = sum(s_and_s_word_dict.values())
    print(f"{sum(s_and_s_word_dict.values())} words in \"Sense_and_Sensibility_Chapter_1.txt\"")

    # print the average sentence length to the console
    print(
        f"The average length of sentence in \"Sense_and_Sensibility_Chapter_1.txt\" is {num_of_words / num_of_sentences:.2f} words")

