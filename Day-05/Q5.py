N = int(input("Enter the value of N:"))
if N <= 1:
    print("Not prime")
else:
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")