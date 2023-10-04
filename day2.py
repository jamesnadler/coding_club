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

# While Loops
while x == 5:
    x = int(input("Enter a number: "))


# Lists
people = ["baron", "aji", "matthew"]
for person in people:
    print(person + " is fruity")

while True:
    direction = input("Where are you going? left, right, or forward: ")
    print("You went " + direction)
    if direction == "left":
        print("Kill yourself")
        break
    if direction == "right":
        print("Nice choice")
        break