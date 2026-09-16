import time
from functools import reduce

# Lambda function representing the linear function: Y = X/2 + 2
linear_func = lambda x: (x / 2) + 2

# 2. Use map as a higher-order function to create a new list
nums = list(range(10001))
mapped_list = list(map(linear_func, nums))

# 3. Sum the elements using reduce and compare times
start_hof = time.time()
sum_hof = reduce(lambda a, b: a + b, mapped_list)
end_hof = time.time()

start_imp = time.time()
sum_imp = 0
for num in mapped_list:
    sum_imp += num
end_imp = time.time()

print(f"Sum (HOF): {sum_hof}, Time: {end_hof - start_hof:.5f} sec")
print(f"Sum (Imperative): {sum_imp}, Time: {end_imp - start_imp:.5f} sec")

# 4. Perform mapping and summing using a single HOF
single_hof_result = reduce(lambda acc, x: acc + linear_func(x), nums, 0)
print(f"Single HOF Result: {single_hof_result}")