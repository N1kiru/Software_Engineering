#Zadanie6

import re

def strip_punctuation_ru(data):

    return re.sub(r'[^\w\s]', '', data)

if __name__ == "__main__":
    import sys

    data = sys.stdin.read().strip()
    print(strip_punctuation_ru(data))