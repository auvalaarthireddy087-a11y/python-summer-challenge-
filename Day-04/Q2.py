try:
    s = input("Enter a number: ").strip()
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

for i in range(1, 11):
    print(f"{N} x {i} = {N * i}")