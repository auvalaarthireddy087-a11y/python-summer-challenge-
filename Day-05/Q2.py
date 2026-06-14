def multiplication_table(N):
    for i in range(1, 11):
        product = N * i
        print(f"{N} x {i} = {product}")

print("Multiplication table for 5:")
multiplication_table(5)