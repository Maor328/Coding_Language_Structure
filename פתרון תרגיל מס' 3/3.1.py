import sys

# Increase recursion limit to handle 1000 calls safely
sys.setrecursionlimit(2000)

# 1. Regular Recursion
def create_tuple_reg(curr, limit):
    if curr > limit:
        return ()
    return (curr,) + create_tuple_reg(curr + 1, limit)

# 2. Tail Recursion
def create_tuple_tail(curr, limit, acc=()):
    if curr > limit:
        return acc
    return create_tuple_tail(curr + 1, limit, acc + (curr,))

# Generate the tuples
tuple_1000_reg = create_tuple_reg(1, 1000)
tuple_1000_tail = create_tuple_tail(1, 1000)