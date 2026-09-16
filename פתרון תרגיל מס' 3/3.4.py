# 1. Regular Recursion
def is_palindrome_number_reg(n):
    s = str(n)
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_number_reg(s[1:-1])

# 2. Tail Recursion
def is_palindrome_number_tail(n, left=0, right=None):
    s = str(n)
    if right is None:
        right = len(s) - 1
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return is_palindrome_number_tail(s, left + 1, right - 1)