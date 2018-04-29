import os
os.system('cls')

# Data Types
# Strings
# Numbers
# Lists
# Tuples
# Dictionaries

#Strings
first_name = "jOhn is"
print(first_name)
print(first_name.upper())
print(first_name.lower())
print(first_name.capitalize())
print(first_name.title())
print(first_name.swapcase())
print(len(first_name))
print(first_name[1])
print(first_name[1:4])
print(first_name[4:len(first_name)]) #position to length of character
print(first_name.split(' '))
print(first_name.split(' ')[1])

#Numbers
var_number = 39
print(var_number)

#Lists
var_lists = ["item 1", "item 2", "item 3"]
print(var_lists)
print(var_lists[1])

#Tuples  (These are immuteable)
var_tuples = ("tuple item 1", "tuple item 2", "tuple item 3")
print(var_tuples)
print(var_tuples[1])

#Dictionaries  (looks like a json object)
var_dict = {
	"Name" : "Lizard",
	"Id" : 17,
	"Title" : "King"
}
print(var_dict)
print(var_dict["Name"])