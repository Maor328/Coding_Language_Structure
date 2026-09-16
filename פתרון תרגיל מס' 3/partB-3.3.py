import math

# Taylor series for e^x using a generator
def taylor_e_generator(x):
    n = 0
    current_sum = 0
    while True:
        # Calculate the next term and add it to the running sum
        current_sum += (x ** n) / math.factorial(n)
        yield current_sum
        n += 1

# Example usage matching the instructions for e^2:
gen = taylor_e_generator(2)
for _ in range(8):
    print(next(gen))