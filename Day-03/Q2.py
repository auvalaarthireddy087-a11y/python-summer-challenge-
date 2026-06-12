available_balance = float(input("Enter your available balance: "))
withdrawal_amount = float(input("Enter the withdrawal amount: "))
if withdrawal_amount <= available_balance:
    available_balance -= withdrawal_amount
    print("Withdrawal successful. Remaining balance:", available_balance)
else:
    print("Insufficient balance. Withdrawal failed.")
