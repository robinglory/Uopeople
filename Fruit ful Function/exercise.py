#exercie 6.2
# def ackerman(m,n):
#     if m == 0:
#         return n+1
#     elif m>0 and n == 0:
#         return m-1,1
#     elif m>0 and n>0:
#         return m-1, m, n-1
#     else:
#         return "False"

# print(ackerman(9,3))

# exercise 6.3

# def first(word):
#     """Returns the first character of a string."""
#     return word[0]


# def last(word):
#     """Returns the last of a string."""
#     return word[-1]


# def middle(word):
#     """Returns all but the first and last characters of a string."""
#     return word[2:-1]


# def is_palindrome(word):
#     """Returns True if word is a palindrome."""
#     if len(word) <= 1:
#         return True
#     if first(word) != last(word):
#         return False
#     return is_palindrome(middle(word))

# print(middle('Helo'))
# print(is_palindrome('allen'))
# print(is_palindrome('bob'))
# print(is_palindrome('otto'))
# print(is_palindrome('redivider'))