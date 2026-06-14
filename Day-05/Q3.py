N = int(input("Enter the value of N:"))
count = 0
if N == 0:
    count = 1
while N > 0:
    N //= 10
    count += 1
print(count)