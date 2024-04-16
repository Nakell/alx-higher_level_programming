#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dict = sorted(a_dictionary.items(), key=lambda item: item[0])
    for key, value in sort_dict:
        print(key + ":", value)
