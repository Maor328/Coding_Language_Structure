def is_prime(n):
    # Numbers less than 2 are not prime
    if n < 2: return False
    # Check for factors up to the square root of n for efficiency
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def get_twin(n):
    # Return n + 2 if both n and n + 2 are prime numbers
    if is_prime(n) and is_prime(n + 2):
        return n + 2
    return None

def twins_dict(n):
    # Create a dictionary of prime numbers and their twins up to n
    return {i: i + 2 for i in range(2, n + 1) if is_prime(i) and is_prime(i + 2)}

# Main script
num_input = input("enter number:\n")
if not num_input.isdigit():
    print("invalid input")
else:
    twin = get_twin(int(num_input))
    if twin:
        print(twin)
    else:
        print("invalid input")