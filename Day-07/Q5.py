numbers = [1, 2, 3, 4, 5, 6]
even_sum = 0
odd_sum = 0
for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
print("Difference between the sum of even and odd numbers:", even_sum - odd_sum)
