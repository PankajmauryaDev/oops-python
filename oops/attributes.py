class student:
    collage_name = "ABC collage"  # class attributes
    pi = 3.1
    def __init__(self , name , gpa):
        self.name = name            # instance attributes.
        self.gpa = gpa
        self.pi = 3.14
std1 = student("pankaj",7.2)

print(std1.name)
# print(student.collage_name)
# print(std1.collage_name)

print(std1.pi)
print(student.pi)
