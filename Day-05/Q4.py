N = int(input("Enter the value of N:"))
reversed_num = 0
while N > 0:
    digit = N % 10
    reversed_num = reversed_num * 10 + digit
    N //= 10
print(reversed_num)