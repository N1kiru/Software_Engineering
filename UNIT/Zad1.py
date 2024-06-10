#Zadanie1

def is_palindrome(data):
    return data == data[::-1]

def test_is_palindrome():
    test_cases = [
        ("deed", True),
        ("nun", True),
        ("level", True),
        ("ab", False),
        ("aba", True),
        ("deified", False),
        ("sagas", True),
        ("RaceCar", False),
        ("A man a plan a canal Panama", False)
    ]

    all_tests_passed = True

    for data, expected in test_cases:
        result = is_palindrome(data)
        if result != expected:
            all_tests_passed = False
            break

    if all_tests_passed:
        print("YES")
    else:
        print("NO")

test_is_palindrome()