# Polling

favorite_languages= {'Jen': 'Python', 'Noel': 'C++', 'Sarah': 'C', 'Edward': 'Rust'} 

friends = ['Noel', 'Edward']
friends_1= ['Jen', 'Sarah']

for name in favorite_languages.keys():
   if name in friends:
      print(f"\t{name.title()}, thank you for taking the poll!\n")

for name in favorite_languages.keys():
   if name in friends_1:
      print(f"\t{name.title()}, can you please take the poll?\n")

  

    
      
