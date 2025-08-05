#List, Tuple, Set, and Dictionary

# List -->- Ordered, mutable, and allows duplicates   
# Common Methods: append(), insert(), remove(), pop(), sort(), reverse()
my_list = [1, 2, 3, 4, 5]

# Tuple -->- Ordered, immutable, and allows duplicates
# Common Methods: count(), index()
my_tuple = (111, 2, 3, 4, 5)

# Set -->- Unordered, mutable, and does not allow duplicates
# Common Methods: add(), remove(), pop(), union(), intersection()
my_set = {1, 2, 3, 4, 5}

# Dictionary -->- Unordered, mutable, and stores key-value pairs
# Common Methods: keys(), values(), items(), get(), pop()
my_dict = {"name": "Ashish", "age": 22, "height": 5.9} 


print("First element in list:", my_list[0])  


print("First element in tuple:", my_tuple[0])


print("Set elements:", my_set)


print("Name from dictionary:", my_dict["name"])



my_list.append(6)
print("Updated list:", my_list) 

my_set.add(6)
print("Updated set:", my_set)

my_dict["weight"] = 70
print("Updated dictionary:", my_dict)


my_list.remove(3)
print("List after removing an element:", my_list)

my_set.remove(3)
print("Set after removing an element:", my_set)

my_dict.pop("age")
print("Dictionary after removing a key-value pair:", my_dict)



for item in my_list:
    print("List item:", item)   

for item in my_tuple:
    print("Tuple item:", item)

for item in my_set:
    print("Set item:", item)

for key, value in my_dict.items():
    print("Dictionary item - Key:", key, ", Value:", value)     
