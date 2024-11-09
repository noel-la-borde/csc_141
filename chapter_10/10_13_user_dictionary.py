# User Dictionary 
import json
from pathlib import Path

def user_info():
    username = input("What is your username? ")
    favorite_color = input("What is your favorite color? ")
    favorite_number = input("What is your favorite number? ")

    user_info = {
        'username': username,
        'favorite_color': favorite_color,
        'favorite_number': favorite_number
    }

    
    path = Path('user_info.json')
    path.write_text(json.dumps(user_info))

def display_user_info():
    
    path = Path('user_info.json')

    
    if path.exists():
        
        user_info = json.loads(path.read_text())
        
       
        print("\nHere's the user summary: ")
        print(f"Username: {user_info['username']}")
        print(f"Favorite Color: {user_info['favorite_color']}")
        print(f"Favorite Number: {user_info['favorite_number']}")
    else:
        print("No user information found. Please provide your details first.")


user_info()  
display_user_info()  

# I did this one following the examples from the book. 