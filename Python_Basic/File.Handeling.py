# File Handling 
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a file handling example in Python.\n") 

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)     

with open('example.txt', 'a') as file:
    file.write("Appending a new line to the file.\n")  

with open('example.txt', 'r') as file:
    content = file.readlines()
    print("File content after appending:")

for line in content:
        print(line.strip()) 
# Reading a specific line from the file
with open('example.txt', 'r') as file:
    lines = file.readlines()    
    if len(lines) > 1:
        print("Second line:", lines[1].strip())