# Lottery 
import random

lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

lucky_ticket = random.sample(lottery_pool, 4)

print("Winning ticket numbers and letters are:", lucky_ticket)
print("Any ticket matching these 4 numbers & letters wins a prize!")

# Very simple code using tupple to store those values. 