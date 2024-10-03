# Shrinking guest list 

names= ['Weliver','Bryant','Angel', 'Luis', 'Leandro']

message= f"Hi {names[0]}, would you like to come for dinner?"
print (message)
message= f"Hi {names[1]}, would you like to comre for dinner?"
print (message)
message= f"Hi {names[2]}, would you like to come for dinner?"
print (message) 
message= f"Hi {names[3]}, would you like to come for dinner?"
print (message) 
message= f"Hi {names[4]}, would you like to come for dinner?\n"
print (message) 

# Name of the guest who can't make it. 
message= f" {names[2]}, won't be able to make it." 
print (message)
message= f" {names[3]}, won't be able to make it.\n" 
print (message) 

# New list with the names of the new guests invited. 

newnames= ['Weliver','Bryant','Pedro', 'Carlos', 'Leandro']

message= f"Hi {newnames[0]}, would you like to come for dinner?"
print (message)
message= f"Hi {newnames[1]}, would you like to come for dinner?"
print (message)
message= f"Hi {newnames[2]}, would you like to come for dinner?"
print (message)
message= f"Hi {newnames[3]}, would you like to come for dinner?"
print (message)
message= f"Hi {newnames[4]}, would you like to come for dinner?\n"
print (message)

# print() call informing that I found a bigger table. 

message= "Hello everyone, I found a bigger table\n"
print (message)

# Adding new guests to the invitation list. 

newnames.insert(0,'Juan')
newnames.insert(2,'Jose')
newnames.append('Noel')

# New set of invitatiom messages with more people added.  

message= f"Hi {newnames[0]}, would you like to come for dinner?"
print (message)
message= f"Hi {newnames[1]}, would you like to come for dinner?"
print (message)
message= f"Hi {newnames[2]}, would you like to come for dinner?"
print (message)
message= f"Hi {newnames[3]}, would you like to come for dinner?"
print (message)
message= f"Hi {newnames[4]}, would you like to come for dinner?"
print (message)
message= f"Hi {newnames[5]}, would you like to come for dinner?"
print (message)
message= f"Hi {newnames[6]}, would you like to come for dinner?"
print (message)
message= f"Hi {newnames[7]}, would you like to come for dinner?\n"
print (message)

# Shrinking print() message. 
message= "Now I can only invite two people\n"
print (message)

# Showing each name I pop from my list with a message. 

popped_guests= newnames.pop()
print (f" {popped_guests}, Im sorry but I don't have enough room for you.")

popped_guests= newnames.pop()
print (f" {popped_guests}, Im sorry but I don't have enough room for you.")
popped_guests= newnames.pop()
print (f" {popped_guests}, Im sorry but I don't have enough room for you.")
popped_guests= newnames.pop()
print (f" {popped_guests}, Im sorry but I don't have enough room for you.")
popped_guests= newnames.pop()
print (f" {popped_guests}, Im sorry but I don't have enough room for you.")
popped_guests= newnames.pop()
print (f" {popped_guests}, Im sorry but I don't have enough room for you.\n")

# Names of the two remaining guests listed with a message. 
print (f"{newnames[0]}, you are more than welcome to come over to dinner")
print (f"{newnames[1]}, you are more than welcome to come over to dinner")

# Removing the two remaining names from my list. 
del newnames[0]
del newnames[0]

# Printing the empty list 
print (newnames)
