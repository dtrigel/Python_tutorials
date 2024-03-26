# Learning Python coding in 2023
# Codemy.com

import os
os.system('cls')

######################
# DATA TYPES
# Strings
# Numbers
# Lists
# Tuples
# Dictionaries
# Boolean
#######################

fist_name = "Daniel" # String
age = 32 # Number
names = ["Daniel", "Guillermo", "Cesar", 23, 32] # List --> they start from zero always
NAME_1 = ("Daniel", "Guillermo", "Cesar") # A tuple is a list tha we cannot change. we cannot add or remove like we can do with lists
fav_pizza = {
    "Daniel"    : "Margheritta",
    "Guillermo" : "Diavola",
    "Cesar"     : "focaccia"
} # Dictionaries are a sort of more complicated lists. the use a key and a value. In this exmple we want a dictionary of Daniel, Guillermo and Cesar's favorite pizzas

logic = True # A boolean is either true or false

print (names[0]) # here we print the list
print (NAME_1) # we can print a tuple in the same manner as with a list
print (fav_pizza["Daniel"]) # We print Daniel's favorite pizza

