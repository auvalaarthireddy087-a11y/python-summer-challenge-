def count_digits(N):
    count = 0
    if N == 0:
        return 1
    N = abs(N)
    while N > 0:
        N //= 10
        count += 1
    return count

result = count_digits(12345)
print(f"Number of digits in 12345 is {result}")