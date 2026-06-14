try:
    N = int(input("Enter the value of N:"))
except Exception:
    # No interactive input available (or invalid). Use a default for testing.
    N = 10

for i in range(1, N + 1):
    if i % 2 == 0:
        print(i)