import os

os.system("cls")

# While Loops

counter = 0
while counter < 10:
    print("The Count is: %s" % counter)
    counter += 1


# For Loops
name = "John"
for x in name:
    print(x)


name_list = ["John", "Bob", "Tina"]
for ind in name_list:
    print(ind)

dict = {"Name": "John", "Age": 31, "Gender": "M"}

for key, value in dict.items():
    print(key)
    print(value)
