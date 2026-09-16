def normalize_text(text):
    # Remove spaces, convert to lowercase, and sort the characters alphabetically
    return "".join(sorted(text.replace(" ", "").lower()))

def are_anagrams(text1, text2):
    # Compare the normalized versions of both strings
    return normalize_text(text1) == normalize_text(text2)

# Main script
t1 = input("enter first text:\n")
t2 = input("enter second text:\n")

# Check if inputs are empty or contain only whitespaces
if not t1.strip() or not t2.strip():
    print("invalid input")
else:
    print(are_anagrams(t1, t2))