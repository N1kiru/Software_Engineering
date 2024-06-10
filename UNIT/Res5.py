#Zadanie5

def strip_punctuation_ru(data):
    import re

    return re.sub(r'[^\w\s]', '', data)

def test_strip_punctuation_ru():

    assert strip_punctuation_ru("Привет, мир!") == "Привет мир"
    assert strip_punctuation_ru("Здравствуй, как дела?") == "Здравствуй как дела"
    assert strip_punctuation_ru("Это - тестовая строка.") == "Это  тестовая строка"
    assert strip_punctuation_ru("Привет... Как ты?") == "Привет Как ты"
    assert strip_punctuation_ru("Здравствуйте, товарищи!") == "Здравствуйте товарищи"

    print("YES")

try:

    test_strip_punctuation_ru()
except AssertionError:

    print("NO")