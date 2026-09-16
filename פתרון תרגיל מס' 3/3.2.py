import sys
sys.setrecursionlimit(2000)

# Helper to generate the tuple so the file runs independently
def create_tuple_tail(curr, limit, acc=()):
    if curr > limit:
        return acc
    return create_tuple_tail(curr + 1, limit, acc + (curr,))

tuple_1000 = create_tuple_tail(1, 1000)

# 1. Regular Recursion
def sum_tuple_reg(tup):
    if not tup:
        return 0
    return tup[0] + sum_tuple_reg(tup[1:])

# 2. Tail Recursion
def sum_tuple_tail(tup, acc=0):
    if not tup:
        return acc
    return sum_tuple_tail(tup[1:], acc + tup[0])

print("Sum (Regular):", sum_tuple_reg(tuple_1000))
print("Sum (Tail):", sum_tuple_tail(tuple_1000))