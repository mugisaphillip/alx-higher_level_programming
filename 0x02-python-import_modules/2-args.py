#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    if length == 0:
        print("0 argument.")
    elif length == 1:
        print("0 argument.")
    else:
        print("{} arguments:".format(length))

    for i in range(, length):
        print("{}: {}".format(i + 1, argv[i + 1]))
