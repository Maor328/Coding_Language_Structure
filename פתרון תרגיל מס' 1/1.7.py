# Define unary mathematical functions
def mul_by_2(x): return x * 2
def square(x): return x ** 2

# Handle division by zero to avoid exceptions
def inverse(x): return 1 / x if x != 0 else None

# Store the functions in a list
funcs_list = [mul_by_2, square, inverse]

def apply_functions(numbers, funcs):
    # Create a dictionary where the key is the function's name (__name__)
    # and the value is the list of results after applying the function
    return {f.__name__: [f(n) for n in numbers] for f in funcs}