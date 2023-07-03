#!/usr/bin/python3
""" Function to indent some text """


def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of the characters '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    Examples:
        >>> text_indentation("Hello. How are you? I am fine.")
        Hello
        How are you
        I am fine

        >>> text_indentation("Python is awesome! What do you think?")
        Python is awesome
        What do you think

        >>> text_indentation("This is a: sample text.")
        This is a
        sample text

        >>> text_indentation(123)
        Traceback (most recent call last):
        ...
        TypeError: text must be a string

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = ['.', '?', ':']
    lines = text.splitlines()

    for line in lines:
        line = line.strip()
        if line:
            for mark in punctuation_marks:
                if mark in line:
                    parts = line.split(mark)
                    indented_line = '\n\n'.join([part.strip() for part in parts])
                    print(indented_line)
                    break
            else:
                print(line, end='')
