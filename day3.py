# Lists Functions
mylist = [ "One", "Two", "Three", "Four" ]
print(mylist)

# List Length
print(len(mylist))

# Append value to list
mylist.append("Five") # append means to add to the end of the list
print(mylist)
print(len(mylist))

# Insert value to list
mylist.insert(0, "Zero")
print(mylist)
print(len(mylist))

awesomelist = [ "we live", "we love", "we lie"]
print(awesomelist)

# Combine lists
secList = [ "Six", "Seven", "Eight", "Nine" ]
mylist.extend(secList)
print(mylist)
print(len(mylist))

# Removing value from list

# Remove by name
mylist.remove("Nine")
print(mylist)
print(len(mylist))

# Remove by index
mylist.pop(0)
print(mylist)