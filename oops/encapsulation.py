# class BankAccount:

#     def __init__(self , name , balance):
#         self.name = name # public
#         self._balance = balance   # protected
#         self.__balance = balance  # private  -- data manging       

#     def get_data(self):
#         return self.__balance
        
# acc1 = BankAccount("pankaj kumar" , 100_000)

# print(acc1.name)    #public data access
# print(acc1._balance) #protected data access
# # print(acc1.__balance) # private data accesss
# # print(acc1._BankAccount__balance) # u can access the data but this is not correct way.

# print(acc1.get_data())  # getter


###############################################################

class BankAccount:

    def __init__(self , name , balance):
        self.name = name # public
        self._balance = balance   # protected
        self.__balance = balance  # private  -- data manging       

    def get_data(self):        # getters 
        return self.__balance
    
    def update_balance(self , amount):
        self.__balance = amount + self.__balance
        print(self.__balance)
            
acc1 = BankAccount("pankaj kumar" , 100_000)

print(acc1.name)

print(acc1.get_data())  # getter

acc1.update_balance(500)  # setters