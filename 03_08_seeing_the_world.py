# Seeing the world 

places= ['Eiffel Tower', 'Burj Khalifa building', 'Downtown Miami', 'Cancun, Mexico', 'Machu Picchu']
print (places[0])
print (places[1])
print (places[2])
print (places[3])
print (places[4])

print ("\n Here is the sorted list:")
print (sorted(places))

print ("\n Here is the original list:")
print (places)

places.reverse()
print ("\n Here is the reversed list:")
print (places)
places.reverse()
print ("\n Here is the original list:")
print (places)

places.sort()
print ("\n Here is the sorted list in alphabetical order:")
print (places)

places.sort(reverse=True)
print ("\n Here is the sorted list in reversed alphabetical order:")
print (places)