import math
from functools import reduce

# a. Function returning a lambda function that calculates base^exp
def power_function(exp):
    return lambda base: base ** exp

# b. Function returning a map object of power functions up to max_exp
def get_power_funcs(max_exp):
    return map(power_function, range(max_exp))

# c. Taylor approximation for e^x using HOFs, no loops or lists
def taylor_e(x, terms):
    funcs_map = get_power_funcs(terms)
    
    # Calculate terms: (x^n) / n! using enumerate to get the index (n)
    term_values = map(lambda f_tuple: f_tuple[1](x) / math.factorial(f_tuple[0]), enumerate(funcs_map))
    
    return reduce(lambda a, b: a + b, term_values)

# Main script: Get the highest power
n_str = input("Enter number of powers:\n")
if n_str.isdigit():
    n = int(n_str)
    result_map = get_power_funcs(n)
    print(type(result_map))
    
    # Get the base and apply the mapped functions
    base_str = input("Enter base:\n")
    if base_str.isdigit():
        base = int(base_str)
        results = tuple(map(lambda f: f(base), result_map))
        print(results)