balance=5000
amt=int(input("Enter the amount to be withdrawn:"))

if(amt<balance and amt%100==0):
    balance-=amt
    print("Withdrawal sucesseful", end=" ")
    print("Remaining balance is:", balance)
elif(amt>balance):
    print("Insufficient balance")
else:
    print("Please enter the amount in multiples of 100")

