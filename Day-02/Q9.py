a = float(input("Enter a number:"))
b = float(input("Enter another number:"))
c = float(input("Enter another number:"))
if a > b and a > c:
    print("a is the greatest")
elif b > a and b > c:
    print("b is the greatest")
else:
    print("c is the greatest")