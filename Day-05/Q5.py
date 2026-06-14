def is_prime(N):
    if N <= 1:
        return False
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            return False
    return True

try:
    N = int(input("Enter a number: ").strip())
except Exception:
    print("Invalid input; please enter a valid integer.")
    exit(0)

if is_prime(N):
    print(f"{N} is Prime")
else:
    print(f"{N} is Not prime")