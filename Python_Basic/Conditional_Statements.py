# If 
age = 16
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Else If 
age = 34
if age < 13:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
else:
    print("You are an adult")

# Nested If 
age = 20
if age >= 18:
    print("You are an adult")
    if age < 21:
        print("You are not old enough to drink alcohol") 
    else:
        print("You can drink alcohol")
else:
    print("You are a minor")        

#Ternary Operator in Python
marks = 45
result = "Pass" if marks >= 40 else "Fail"
print(result)
