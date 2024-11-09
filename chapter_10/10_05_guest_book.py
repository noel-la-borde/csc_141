# Guest Book

from pathlib import Path

path = Path('guest_book.txt')

while True:
    name = input("What's your name? ")
    path.write_text(name)
    print(f"Welcome, {name}! Your name has been added to the guest book.")

'''
I was a little bit confused doing the while loop and the book doesn't 
provide specific examples for this exercise, but I took a look at the 
book's answers in the github account provided by Professor Kaul.  
'''