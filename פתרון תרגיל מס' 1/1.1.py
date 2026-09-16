def get_penta_num(n):
    # Calculate the penta number using the formula: n(3n-1)/2
    # Using integer division (//) to return an int instead of a float
    return n * (3 * n - 1) // 2

def pentaNumRange(n1, n2):
    # Return a list of penta numbers in the range from n1 to n2 (exclusive)
    return [get_penta_num(i) for i in range(n1, n2)]