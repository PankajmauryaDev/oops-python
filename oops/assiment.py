# Concept: Classes & Objects

# Q1. Create a BankAccount class with attributes account_number,
#  owner_name, and balance.
# Add methods to deposit, withdraw, and check balance.

class bankAccount:
    
    def __init__(self , account_number , owner_name , balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    
    def deposite(self , amount):
        update_balance = amount + self.balance
        print(update_balance)
    
    def withdrow(self , amount):
        remain_balance = self.balance - amount 
        print(remain_balance)

acc1 = bankAccount("25scse2030490" , "Pankaj" , 30_0000)
print(acc1.owner_name)

print(acc1.balance)

acc1.deposite(100)

acc1.withdrow(200)

#####################################################################

# Q2. Create a class Book with the following attributes:
# title
# author
# list of reviews

# And add methods to:

# add a new review
# count reviews
# display all reviews        