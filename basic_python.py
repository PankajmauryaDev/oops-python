# 1. Print
print("Welcome to Python")

# 2. Variables & Data Types
name = "Pankaj"
age = 21
price = 99.5
is_student = True

print("Name:", name)
print("Age:", age)
print("Price:", price)
print("Student:", is_student)

# 3. Input
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

# 4. Conditional Statements
if user_age >= 18:
    print(user_name, "is an Adult")
elif user_age == 17:
    print(user_name, "is Almost Adult")
else:
    print(user_name, "is Minor")

# 5. For Loop
print("\nFor Loop:")
for i in range(5):
    print(i)

# 6. While Loop
print("\nWhile Loop:")
i = 0
while i < 5:
    print(i)
    i += 1

# 7. Function
def add(a, b):
    return a + b

result = add(5, 3)
print("\nSum:", result)

# 8. List
numbers = [10, 20, 30, 40]
print("\nList elements:")
for num in numbers:
    print(num)

# 9. Operators
a = 10
b = 3
print("\nOperators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Floor Division:", a // b)
print("Power:", a ** b)

# 10. Comment Example
# This is a single-line comment

print("\nProgram Finished")
