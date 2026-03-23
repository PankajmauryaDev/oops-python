# class employee:
#     st_time = "10am"
#     end_time = "5pm"

#     def change_time(self , new_end_time):
#         self.end_time = new_end_time

# class teacher(employee):

#     def __init__(self , subject):
#         self.subject = subject


# t1 = teacher("math")
# t1.change_time("8pm")
# print(t1.subject , t1.st_time , t1.end_time)

#####################################################################


# class employee:
#     st_time = "10am"
#     end_time = "5pm"

#     def change_time(self , new_end_time):
#         self.end_time = new_end_time

# class teacher(employee):

#     def __init__(self , subject):
#         self.subject = subject


# class staff(teacher):

#     def __init__(self , role):
#         self.role = role

# stf1 = staff("accountant")

# print(f"role : {stf1.role} entry : {stf1.st_time} exit : {stf1.end_time}")

######################################################################################

                # types of inheritance

# class employee:
#     st_time = "10am"
#     end_time = "5pm"

#     def change_time(self , new_end_time):
#         self.end_time = new_end_time

# class teacher(employee):

#     def __init__(self , subject):
#         self.subject = subject

# class accountant(teacher):

#     def __init__(self , salary , role):
#         self.salary = salary
#         super().__init__(role)

# acc1 = accountant(25_000 , "CA")

# print(acc1.subject )

#######################################################################

# multiple inheritance.

class teacher:
    def __init__(self , salary):
        self. salary = salary

class student:
    def __init__(self , gpa):
        self.gpa = gpa

class TA( teacher , student):

    def __init__(self, salary , gpa , name):
        super().__init__(salary)
        student.__init__(self, gpa)
        self.name = name


ta1 = TA(25_000 , 6.4 , "Pankaj")

print(ta1.name , ta1.salary ,ta1.gpa)