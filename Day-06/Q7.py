arr = list(map(int, input().split()))
count_greater_than_10 = 0
for num in arr:
    if num > 10:
        count_greater_than_10 += 1
        print(count_greater_than_10)