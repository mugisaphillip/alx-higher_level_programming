#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for ltr in my_string:
        if ltr not in ["c", "C"]:
            new_str += ltr
    return new_str
