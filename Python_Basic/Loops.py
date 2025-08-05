#  simple loop in Python.
import Hospital_Management_System as hms

hms.main()


for i in range(5):
    print("Iteration:", i)

# While loop 
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

# Nested loop in Python
for i in range(5):
    for j in range(2):
        print("i:", i, "j:", j, "Product:", i * j)

        