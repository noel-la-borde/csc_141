# Adition Calculator

print("Give me two numbers, and I'll add them.")

print("Enter 'q' to quit.")


first_number = input("\nFirst number: ")
if first_number != 'q':
    second_number = input("Second number: ")

    if second_number != 'q':
        try:
            answer = int(first_number) + int(second_number)
    
        except ValueError:
            print("\n Please enter a valid input") 
        else:
            print(f"The answer is: {answer}")

# This one was a tricky but the book does provide examples for this one. 