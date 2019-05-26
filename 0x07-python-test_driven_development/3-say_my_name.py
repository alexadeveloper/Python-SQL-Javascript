#!/usr/bin/python3
"""Simple function"""


def say_my_name(first_name, last_name=""):
    """function to say my name


    Args:
        first_name (string): the first name
        last_name (string): the last name

    Return:
        Nothing
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
