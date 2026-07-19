import math
# String data type

# Literal assignment
first = "Hope"
last = "Georgewill"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# construction function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
fullname= first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string

decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
Hey, how are you?

I was just checking in.
                        All good?

'''
# print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
# print(sentence) 

# String Methods

# print(first.lower())
# print(first.upper())
# print(first)

# print(multiline.title())
# print(multiline.replace("good", "ok"))
# print(multiline)

# print(len(multiline))
# add white space
multiline += "                                           "
multiline = "                  " + multiline
# print(len(multiline))

#remove white space
# print(len(multiline.strip()))
# print(len(multiline.lstrip()))
# print(len(multiline.rstrip()))

# Build a menu
title = "menu".upper()
print("")
#places the value at the center of 20 equal to symbols
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Chessecake".ljust(16, ".") + "$4".rjust(4))

# string index values

#first value in a string
print(first[0])

#last value in a string
print(first[-1])
print(first[1:-1])
print(first[1:])

#Some methods return boolean data
print(first.startswith("F"))
print(first.startswith("H"))
print(first.endswith("e"))

#boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

#Numeric data types

# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

#float type
gpa = 3.28
y = float(1.14)
print(type(gpa))
print(isinstance(y, float))

#complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers

print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))


print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

#Casting a string to a number
zipcode = "5000001"
zip_value = int(zipcode)
print(type(zip_value))

#Error if you attempt to cast incorrect data
# zip_value = int("New York")