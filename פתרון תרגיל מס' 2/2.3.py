def is_armstrong(n):
    # Pure function to check if a number is an Armstrong number
    str_n = str(n)
    k = len(str_n)
    # Using HOFs (map, sum) to check the condition
    return sum(map(lambda digit: int(digit) ** k, str_n)) == n

def range_armstrong(n1, n2):
    # Return a list of Armstrong numbers in the given range using filter
    return list(filter(is_armstrong, range(n1, n2 + 1)))

# Main script to get user input
user_input = input("Enter a number:\n")

# Validate that the input is a valid positive integer
if not user_input.isdigit() or int(user_input) <= 0:
    print("input invalid")
else:
    num = int(user_input)
    print(range_armstrong(1, num))