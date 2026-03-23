# product store

# class store:

#         def __init__(self , product , price):
#                 self.product = product
#                 self.price = price

#         def full(self):
#                 print(f"product name is : {self.product} and price {self.price}")

# p1 = store("laptop" , 40_000)
# p1 = store("moblie", 15_000)
# p2 = store("pen" , 10)

# # print(p1.product , p1.price)
# p1.full()


###############################################################################

# class store:
#         count = 0

#         def __init__(self , product , price):
#                 self.product = product
#                 self.price = price
#                 store.count += 1

#         def full(self):
#                 print(f"product name is : {self.product} and price {self.price}")

#         @classmethod
#         def tract(cls):
#                 print(f"{cls.count} object is created")


# p1 = store("laptop" , 40_000)
# p1 = store("moblie", 15_000)
# p2 = store("pen" , 10)

# # print(p1.product , p1.price)
# # p1.full()

# store.tract()

##########################################################################

class store:
        count = 0

        def __init__(self , product , price):
                self.product = product
                self.price = price
                store.count += 1

        def full(self):
                print(f"product name is : {self.product} and price {self.price}")

        @classmethod
        def tract(cls):
                print(f"{cls.count} object is created")
        
        @staticmethod
        def cal_discount(price , discount):
            final_price = price - (price * discount / 100)    
            print(f"final price after discount : {final_price}")           



p1 = store("laptop" , 40_000)
p2 = store("moblie", 15_000)
p3 = store("pen" , 10)

# print(p1.product , p1.price)
# p1.full()

store.tract()

p1.cal_discount(40_000 , 10)

store.cal_discount(p2.price , 10)