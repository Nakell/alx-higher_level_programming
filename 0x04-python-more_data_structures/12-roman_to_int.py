#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    index = 0
    while index < len(roman_string):
        current_value = roman_num.get(roman_string[index], 0)
        if index < len(roman_string) - 1:
            next_value = roman_num.get(roman_string[index + 1], 0)
            if current_value < next_value:
                total += (next_value - current_value)
                index += 2
            else:
                total += current_value
                index += 1
        else:
            total += current_value
            index += 1
    return total
