def reverse_number(N):
    reversed_num = 0
    while N > 0:
        digit = N % 10
        reversed_num = reversed_num * 10 + digit
        N //= 10
    return reversed_num

result = reverse_number(12345)
print(f"Reverse of 12345 is {result}")