from functools import reduce

# Create a list from 1 to 1000
nums = list(range(1, 1001))

# Split into evens and odds using filter
evens = list(filter(lambda x: x % 2 == 0, nums))
odds = list(filter(lambda x: x % 2 != 0, nums))

# 1. Lambdas for each case:
# Evens: multiply accumulated product by the next element
even_lambda = lambda acc, next_val: acc * next_val

# Odds: use the linear function where 'acc' represents the sum
odd_lambda = lambda acc, next_val: (acc / 2) + 2 + next_val

# 2 & 3. Execute and summarize using reduce
evens_result = reduce(even_lambda, evens)
odds_result = reduce(odd_lambda, odds)

print("Evens product length:", len(str(evens_result)), "digits")
print("Odds calculation result:", odds_result)