# Every Function 

cars= ['Honda', 'Toyota','Land Rover', 'Mercedes Benz']

# adding elements to my list
cars.insert(0,'Mazda')
cars.insert(1,'BMW')
cars.append('GMC')
# displaying my list in order
print (cars[0])
print (cars[1])
print (cars[2])
print (cars[3])
print (cars [4])
print (cars [5])
print (cars [6])

# sorting my list 
print ("\n Here is the sorted list:")
print (sorted(cars))

cars.reverse()
print ("\n Here is the reversed list:")
print (cars)

cars.sort()
print ("\n Here is the sorted list in alphabetical order:")
print (cars)

cars.sort(reverse=True)
print ("\n Here is the sorted list in reversed alphabetical order:")
print (cars)

print ("\n Here is the original list:")
print (cars)

# message selecting specific element from a list

message= f"\n My dream car has always been a {cars[4].title()} SUV.\n"
print (message)

# pop() 

popped_cars= cars.pop()
print (f" I'll remove {popped_cars} because I can't afford that maker.") 
print ("\n Here is the modified list:\n")
print (cars)

# del

del cars [3]
print ("\n Here is the modified list after deleting another maker:\n")
print (cars)

# len

len(cars)
print ("\n Number of the remaining makers in my list:\n")
print (len(cars))   