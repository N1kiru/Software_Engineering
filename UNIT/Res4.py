#Zadanie4

import re

def is_correct_mobile_phone_number_ru(number):

    pattern = r"^(8|\+7)(\s?\(?\d{3}\)?\s?|\д{3}\s?)[\д\s-]{7,10}$"
    return bool(re.match(pattern, number))

if __name__ == "__main__":
    import sys

    number = sys.stdin.read().strip()

    if is_correct_mobile_phone_number_ru(number):

        print("YES")
    else:

        print("NO")