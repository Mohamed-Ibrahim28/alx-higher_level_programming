#!/usr/bin/python3

"""New Module For Write a function that reads a text file
(UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """New Function For read File and Print data"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
