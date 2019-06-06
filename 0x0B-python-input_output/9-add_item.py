#!/usr/bin/python3
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    try:
        mylist = load_from_json_file(add_item.json)
    except Exception:
        lista = []
    for i in range(1, len(argv)):
        lista.append(argv[i])
    save_to_json_file(lista, "add_item.json")
