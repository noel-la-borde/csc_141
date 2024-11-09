# Addition Calculator

print("Give me two numbers, and I'll add them.")

print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    
    try:
        answer = int(first_number) + int(second_number)
    
    except ValueError:
        print("\n Please enter a valid input") 
    else:

        print(f"The answer is: {answer}")

# This one was similar to the previous exercise, but in this one I had to store the program inside a while loop.  