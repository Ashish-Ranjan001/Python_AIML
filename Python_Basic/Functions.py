def greet():
    print("Hello World!")

greet()

name=input("Enter your name: ")
def welcome(name):
    print("Welcome, " + name)   

    welcome(name)

def add(a, b):
    return a + b
result = add(5, 10)
print("Sum is:", result)

# Creating an BMI calculator function
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi  
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = calculate_bmi(weight, height)
print("Your BMI is:", bmi)