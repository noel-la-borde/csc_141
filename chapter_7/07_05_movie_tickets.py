# Movie Tickets
message=""

while message!="Quit":
    prompt = "What is your age?"
    message = input(prompt)


    
    if(message !="Quit"):
        age = int(message)
        if age>0 and age<3:
            print("Ticket cost is free")
        elif age>= 3 and age<= 12:
            print("Ticket cost is $10")
        elif age>12:
            print("Ticket cost is $15")
        elif message:
            print("Quit")
    



    
        
    
