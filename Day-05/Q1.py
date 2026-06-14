def sum_of_natural_numbers(N):
    total_sum = 0
    for i in range(1, N + 1):
        total_sum += i
    return total_sum

result = sum_of_natural_numbers(10)
print(f"Sum of natural numbers up to 10 is {result}")