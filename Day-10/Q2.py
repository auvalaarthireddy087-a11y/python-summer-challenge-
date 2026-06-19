n, m = map(int, input().split())
arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
for i in range(n):
    s = 0
    for j in range(m):
        s += arr[i][j]
    print("sum of rows", i, "=", s)
