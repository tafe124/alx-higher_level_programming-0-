#!/usr/bin/python3
def roman_to_int(roman_string):
    arab_num = 0
    symbol = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
              'D': 500, 'M': 1000}

    is_invalid = not isinstance(roman_string, str)\
        or len(roman_string) == 0 or roman_string[0] not in symbol
    if is_invalid:
        pass

    else:
        i = 0
        j = i + 1
        length = len(roman_string)

        while i < length:
            rom_num = roman_string[i]
            value = symbol[rom_num]

            if j == length:
                arab_num += value
                break
            nxt = roman_string[j]

            if nxt not in symbol:
                return 0

            nxt_value = symbol[nxt]

            if nxt_value > value:
                arab_num += nxt_value - value
                i += 1
                j += 1

            else:
                arab_num += value

            j += 1
            i += 1

    return arab_num
