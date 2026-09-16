# Tail recursive RLE encoding
def encode_rle(s, count=1, acc=""):
    if not s:
        return acc
    if len(s) == 1:
        return acc + s[0] + str(count)
    if s[0] == s[1]:
        return encode_rle(s[1:], count + 1, acc)
    # Reset count to 1 when a new character appears
    return encode_rle(s[1:], 1, acc + s[0] + str(count))

# Main Script loop: continues until input is empty or just spaces
while True:
    user_text = input("enter text:\n")
    if not user_text or user_text.isspace():
        print("invalid input")
        break
    else:
        print(encode_rle(user_text))