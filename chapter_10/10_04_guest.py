# Guest 

from pathlib import Path

path= Path('guest.txt')
name= input("what's your name?")
path.write_text(name)

# This exercise is very similar to exercise 10_01 and did it following the instructions from the book. 