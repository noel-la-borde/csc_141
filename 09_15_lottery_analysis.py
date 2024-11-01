# Lottery Analysis

import random


lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

my_ticket = random.sample(lottery_pool, 4)

attempts = 0

while True:
    winning_ticket = random.sample(lottery_pool, 4)
    attempts += 1
    
    if set(winning_ticket) == set(my_ticket):
        break  


print("Your ticket numbers and letters are:", my_ticket)
print("Winning ticket numbers and letters are:", winning_ticket)
print(f"It took {attempts} attempts to win the lottery!")

# This exercise was not too complex for me compared to some of the previous ones.
# I had to use Chat to test my code and search for errors though.