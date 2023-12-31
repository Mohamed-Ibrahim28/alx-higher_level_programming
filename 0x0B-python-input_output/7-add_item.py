#!/usr/bin/python3

"""New Module for adds all args to Py-list, and then save them to JSON-file"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    filename = "add_item.json"
    try:
        re_list = load_from_json_file(filename)
    except FileNotFoundError:
        re_list = []

    re_list.extend(sys.argv[1:])
    save_to_json_file(re_list, filename)
