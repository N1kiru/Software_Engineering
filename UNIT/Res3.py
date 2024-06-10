#Zadanie3

import re

def is_correct_mobile_phone_number_ru(number):

    pattern = r"^(8|\+7)(\s?\(?\d{3}\)?\s?|\d{3}\s?)[\d\s-]{7,10}$"

    return bool(re.match(pattern, number))

def test_is_correct_mobile_phone_number_ru():

    assert is_correct_mobile_phone_number_ru("+7 999 123-45-67") == True
    assert is_correct_mobile_phone_number_ru("8(900)1234567") == True
    assert is_correct_mobile_phone_number_ru("+7(900)1234567") == True
    assert is_correct_mobile_phone_number_ru("+7 900 123 45 67") == True
    assert is_correct_mobile_phone_number_ru("8 900 1234567") == True
    assert is_correct_mobile_phone_number_ru("8 900 123-45-67") == True
    assert is_correct_mobile_phone_number_ru("+7 900 1234567") == True

    assert is_correct_mobile_phone_number_ru("900 1234567") == False
    assert is_correct_mobile_phone_number_ru("7 900 123 45 67") == False
    assert is_correct_mobile_phone_number_ru("+8 900 123 45 67") == False

    print("YES")

try:

    test_is_correct_mobile_phone_number_ru()
except AssertionError:

    print("NO")