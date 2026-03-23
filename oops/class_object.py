# class student:
#     subject = "python"
#     collage = "abc" 
#     year = "4th year student"

# std1 = student()
# std2 = student()
# print(std1.subject)
# print(std2)



############################################################################


# class car:
    # brand = None
    # model = None

    # def __init__(self , car_brand , car_model):
    #     self.brand = car_brand
    #     self.model = car_model

    # def __init__(self , brand , model):                       ee
    #     self.company = brand
    #     self.product = model

   

# my_car = car("toyota" , "cerolla")
# print(my_car.brand , my_car.model)
# print(my_car.company , my_car.product)


# my_new_car = car("tata" , "safari")

# print(my_new_car.company , my_new_car.product)


##################################################################

# class student:
#     print("hello")
#     def __init__(self , name , g_name):
#         print("constructor was called ...")
#         print("world")
#         self.boy_name = name
#         self.girl_name = g_name



# std1 = student("pankaj" , "varsha")
# std2 = student("maurya" , "shakshii")

# print(std1.boy_name , std1.girl_name)



####################################################################


# class student:

#     def __init__(self , std_name , std_cgpa):  #paramiterzied constructor.
#         self.name = std_name
#         self.cgpa = std_cgpa

#     def get_cgpa(self):
#         return self.cgpa

# std1 = student("Pankaj" , "7.6")
# std2 =  student("varsha" , "8.2")

# print(std1.name , std1.cgpa)
# print(std2.name , std2.cgpa)

# # std1 = std1.get_cgpa()

# print(f"{std1.name} cgpa is : {std1.cgpa}")


####################################################

# class car:
#     def __init__(self, name , brand):
#         print("constuctor is called ....")
#         self.company = name
#         self.product = brand

#     def fullname(self):
#         return f"{self.company}  {self.product}"

    


# my_car = car("toyota" , "corolla")
# my_new_car = car("tata" , "safari")
# full_car_name = my_new_car.fullname()

# print(my_car.company , my_new_car.product)
# print(my_new_car.product)
# print(full_car_name)


#####################################################################3

class area:

    def area_cal(self , length , breath):
        self.ar = (length * breath)
        return self.ar
        # print(self.ar)


obj = area().area_cal(10,20)

print(obj)
        

        