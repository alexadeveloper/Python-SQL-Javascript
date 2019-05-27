#!/usr/bin/python3
"""Simple function"""


def text_indentation(text):
    """prints a text with 2 new lines
    Args:
    text (string): the text to prints
    Return:
    Nothing
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.strip()
    for i in range(0, len(text) - 1):
        print(text[i], end='')
        if text[i] == ':' or text[i] == '.' or text[i] == '?':
            print("\n")
            if text[i + 1] == ' ':
                i += 1
            if text[i] == ' ' and text[i + 1] == ' ' and i + 1 < len(text):
                i += 1
        i += 1
