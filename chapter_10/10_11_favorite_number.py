from pathlib import Path
import json

def favorite_number():
    
    favorite_number = input("What is your favorite number? ")
    path = Path('favorite_number.json')
    
   
    contents = json.dumps(favorite_number)
    path.write_text(contents)  

def retrieve_number():
    
    path = Path('favorite_number.json')
    
    
    if path.exists():
       
        contents = path.read_text()
        favorite_number = json.loads(contents)
        print(f"I know your favorite number! It is: {favorite_number}!")

favorite_number()  
retrieve_number()  

# This one was kind of difficult, I had to follow the answers guide from github. 