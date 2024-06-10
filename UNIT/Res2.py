#Zadanie2

def is_palindrome(data):
    return data == data[::-1]

if __name__ == "__main__":

  import sys

  data = sys.stdin.read().strip()

  if is_palindrome(data):
      print("YES")
      print("data = " + "'" + data + "'")
  else:
      print("NO")
      print(data)
      print("data = " + "'" + data + "'")