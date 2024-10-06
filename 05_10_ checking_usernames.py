# Checking Usernames 

current_users= ['Noel', 'Pedro', 'Louis', 'Rosangel']
new_users= ['Louis', 'Joe', 'Kyle', 'Jules']

for current_user in current_users:
  if current_user in new_users:
    print(f"Hello {current_user}, you'll need to enter a new username")
else:
   for new_user in new_users:
     if new_user != 'Louis':
      print(f"\nHello {new_user},the usermane is available")