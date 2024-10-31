class bank:
    def __init__(self,initial_balance):
        self.balance=initial_balance
        with open("account_detail.txt","w") as file:
            file.write(f"The initial balance is:{self.balance}\n")
    
    def credit(self,amount):
     
        self.amount += amount
        with open("account_detail.txt","a") as fi:
            fi.write(f"The amount after credit is:{amount}\n")
            fi.write(f"Balance after credit: {self.balance}\n")
    def debit(self,amount):
        if amount > self.balance:
            print("Insufficient balance!")
            with open("account_detail.txt", "a") as fl:
                fl.write("Debit attempt failed due to insufficient balance.\n")
        else:
            self.balance -= amount
            with open("account_detail.txt", "a") as fe:
                fe.write(f"Debited: {amount}\n")
                fe.write(f"Balance after debit: {self.balance}\n")
    def view_transactions(self):
        print("Transaction History:")
        with open("account_detail.txt", "r") as file:
            print(file.read())

acc2=bank(1000)          
v=acc2.credit(500)
print(v)                            
w=acc2.debit(300)  
print(w)                                  
x=acc2.view_transactions() 
print(x)