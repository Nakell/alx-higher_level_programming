#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = []
    for item in my_list:
        if item not in result:
            result.append(item)
    return sum(result)
