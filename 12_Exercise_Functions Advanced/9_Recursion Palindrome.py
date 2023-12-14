# def palindrome(word, *args):
#     if word == word[::-1]:
#         return F"{word} is a palindrome"
#     else:
#         return F"{word} is not a palindrome"


def palindrome(word, idx):
    if word == word[::-1]:
        return F"{word} is a palindrome"
    else:
        return F"{word} is not a palindrome"







print(palindrome("abcba", 0))
print(palindrome("peter", 0))
