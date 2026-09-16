# 1. Regular Recursion (using GCD)
def gcd_reg(a, b):
    if b == 0:
        return a
    return gcd_reg(b, a % b)

def lcm_reg(a, b):
    return abs(a * b) // gcd_reg(a, b)

# 2. Tail Recursion (direct multiple check)
def lcm_tail(a, b, mult=1):
    if (a * mult) % b == 0:
        return a * mult
    return lcm_tail(a, b, mult + 1)

print("LCM of 6 and 4 (Regular):", lcm_reg(6, 4))
print("LCM of 6 and 4 (Tail):", lcm_tail(6, 4))