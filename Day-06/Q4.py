arr = list(map(int, input().split()))
smallest = arr[0]
for num in arr:
    if num < smallest:
        smallest = num
        print(smallest)