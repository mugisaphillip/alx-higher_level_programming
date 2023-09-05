#!/usr/bin/python3
"""
text_indentation - prints a text with 2 new lines
                   after each of these characters: ., ? and :
@text: text passed
Return: None
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = [".", "?", ":"]
    result = ""
    in_new_line = False

    for char in text:
        if char in chars:
            result += char + "\n\n"
            in_new_line = True
        else:
            if in_new_line and char.isspace():
                continue
            else:
                result += char
                in_new_line = False

    for line in result.split("\n"):
        print(line.strip())
