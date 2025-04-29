class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    #debit method

    def debit(self, amount):
        self.balance -= amount
        print("Rs. amount is :", amount, "Was Debited")
        print("Total balance is :", self.balanced())
        
    def credit(self, amount):
        self.balance += amount
        print("Rs. amount is :", amount, "Was Credited")
        print("Total balance is :", self.balanced())

    def balanced(self):
        return self.balance
    
acc1 = Account(10000, 12345)

print(acc1.balance)
print(acc1.account_no)
print(acc1.credit(2000))
print(acc1.debit(500))