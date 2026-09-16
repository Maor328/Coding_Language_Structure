def sum_digit(num_str):
    # Check if the input string contains only digits
    if not num_str.isdigit():
        return "invalid input"
    # Convert each character to an integer and sum them up
    return sum(int(digit) for digit in num_str)

# Main script
user_input = input("enter number:\n")
print(sum_digit(user_input))