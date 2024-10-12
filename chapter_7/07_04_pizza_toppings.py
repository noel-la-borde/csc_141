# Pizza Toppings 

prompt= "Please enter the toppings you want me to add to your pizza:"
prompt += "\n Enter 'Quit' to end the program."



message = ""
message2 = ""
prompt+= "\n Toppings so far:"
while message != 'Quit':
    message = input(prompt)
    prompt += message + ", "

    

print(message)
