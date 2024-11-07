# Guest 

from pathlib import Path

path= Path('guest.txt')
name= input("what's your name?")
path.write_text(name)