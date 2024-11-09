# Verify User

import json
from pathlib import Path

def get_new_username():

    new_username = input("What is your username? ")
    
    user_info = {'username': new_username}
    path = Path('user_info.json')
    path.write_text(json.dumps(user_info))
    return new_username

def greet_user():
   
    path = Path('user_info.json')
    
    
    if path.exists():
        user_info = json.loads(path.read_text())
        stored_username = user_info['username']
        
       
        correct_username = input(f"Is your username '{stored_username}'? (yes/no): ").strip().lower()
        
        if correct_username == 'yes':
            print(f"Welcome back, {stored_username}!")
        else:
            new_username = get_new_username()
            print(f"Welcome, {new_username}!")
    else:
        
        new_username = get_new_username()
        print(f"Welcome, {new_username}!")


greet_user()

# This one is very long and I did it following an example for this exercise that the book provides. 