try:
    s = input("Enter the value of N: ").strip()
    if s == "":
        print("No input provided; exiting.")
        exit(0)
    N = int(s)
except EOFError:
    print("No input available; exiting.")
    exit(0)
except Exception:
    print("Invalid input; exiting.")
    exit(0)

for i in range(1, N + 1):
    if i % 2 != 0:
        print(i)
