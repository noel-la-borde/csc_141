from pathlib import Path
import json

def get_favorite_number():

    path = Path('favorite_number.json')

    if path.exists():
        
        contents = path.read_text()
        favorite_number = json.loads(contents)
        print(f"I know your favorite number! It is: {favorite_number}!")
    else:
        
        favorite_number = input("What is your favorite number? ")
        contents = json.dumps(favorite_number)
        path.write_text(contents)
        print(f"Now I know your favorite number! It is: {favorite_number}!")

# Not too difficult, but I had to check my code because it wasn't working.
# I Had to correct some errors and follow the answers guide on github. 
