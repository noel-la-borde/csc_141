# Guest Book

from pathlib import Path

path = Path('guest_book.txt')

while True:
    name = input("What's your name? ")
    path.write_text(name)
    print(f"Welcome, {name}! Your name has been added to the guest book.")