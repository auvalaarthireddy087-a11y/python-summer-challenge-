arr = list(map(int, input().split()))
total_sum = 0
for num in arr:
    total_sum += num
    average = total_sum / len(arr)
    print(average)