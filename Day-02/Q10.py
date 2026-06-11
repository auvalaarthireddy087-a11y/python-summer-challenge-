purchase_amount = float(input("Enter the purchase amount:"))
if purchase_amount > 5000:
    discount = purchase_amount * 0.20
    print("Eligible for a 20% discount")
else:
    discount = 0.0
    final_payable = purchase_amount - discount
    print("Final payable amount:",)