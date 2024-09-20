# Slices

# code from 04_08_cubes.py 
cubes= []
for value in range (1,11):
 cubes.append(value **3)
 
# Lines added to the end of the program
print(f" The first three items of the list are the first three cubes:\n{cubes[:3]}")
print(f"\n The middle fourth items of the list are the middle fourth cubes:\n{cubes[3:7]}")
print(f"\n The last three items of the list are the last three cubes:\n{cubes[7:11]}")