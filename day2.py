# Input 
x = int(input("Enter a number: "))
print(x)

# Conditional Statements
y = 4

c = x == 5
print(c)

c = x != 5
print(c)

c = x == 5 and y == 4
print(c)

c = x == 4 or y == 5
print(c)


# If/then statements
if x == 5:
    print("x is equal to 5")
elif x == 6: # elif is short for else if
    print("x is equal to 6")
else:
    print ("x is neither 5 or 6")