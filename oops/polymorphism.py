# example of polymorphirm in py

# print(1+2 , "pankaj " + "Maurya")


# function overriding

class employee:
    def get_role(self):
        print("role = employee")

class teacher(employee):
    def get_role(self):
        print("role = teacher")


# t1 = teacher()
# t1.get_role()

t1 = employee()
t1.get_role()

#######################################################################


