# Tail recursive helper to clean the string 
def clean_str_tail(s, acc=""):
    if not s:
        return acc
    c = s[0].lower()
    # Dictionary for Hebrew end-letters
    hebrew_ends = {'ך': 'כ', 'ם': 'מ', 'ן': 'נ', 'ף': 'פ', 'ץ': 'צ'}
    c = hebrew_ends.get(c, c)
    
    if c.isalnum():
        return clean_str_tail(s[1:], acc + c)
    return clean_str_tail(s[1:], acc)

def is_palindrome_alphanumeric(s):
    cleaned = clean_str_tail(s)
    
    # Pure tail recursive palindrome checker
    def check_pal_tail(text, left, right):
        if left >= right:
            return True
        if text[left] != text[right]:
            return False
        return check_pal_tail(text, left + 1, right - 1)
    
    if not cleaned:
        return True
    return check_pal_tail(cleaned, 0, len(cleaned) - 1)

# Main Script loop: continues until input is empty or just spaces
while True:
    user_input = input("enter text:\n")
    if not user_input or user_input.isspace():
        print("invalid input")
        break
    else:
        print(is_palindrome_alphanumeric(user_input))