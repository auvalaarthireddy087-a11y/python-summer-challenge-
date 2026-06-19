n, m = map(int, input().split())
arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
key = int(input())
found = False
for i in range(n):
    for j in range(m):
        if arr[i][j] == key:
            print("Found at:", i, j)
            found = True
            break
    if found:
        break
if not found:
    print("Not found")
            