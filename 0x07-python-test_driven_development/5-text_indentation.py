#!/usr/bin/python3

"""
    Text Indentation  prints a text with 2 new lines after 
    each of these characters: ., ? and :

"""
def text_indentation(text):

    separators = ".?:"  # Define the separators
    current_word = ""
    words = []

    for char in text:
        if char not in separators:
            current_word += char
        else:
            current_word += char
            words.append(current_word)  # Add the finished word to the list
            current_word = ""  # Reset for the next word

    words.append(current_word)  # Add the last word

    print(words)
