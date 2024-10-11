# People

person_01= {'first_name': 'Bryant', 'last_name': 'Sanchez', 'age': 22, 'city': 'Reading'}
person_02= {'first_name': 'Noel', 'last_name': 'La Borde', 'age': 23, 'city': 'Reading'}
person_03= {'first_name': 'Louis', 'last_name': 'Santana', 'age': 24, 'city': 'Bronx'}

persons= [person_01, person_02, person_03] 

for (key, value) in person_01.items():
     print(f"His {key} is {value}")
print("\n")
for (key, value) in person_02.items():
     print(f"His {key} is {value}")
print("\n")
for (key, value) in person_03.items():
     print(f"His {key} is {value}")
