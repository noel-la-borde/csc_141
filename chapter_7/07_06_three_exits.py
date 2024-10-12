# Three Exits

message=""

while message!="Quit":
    prompt = "What is your shoe size?"
    message = input(prompt)


    
    if(message !="Quit"):
        size = int(message)
        if size>0 and size<=6:
            print("SMALL FEET")
        elif size>=7 and size<= 10:
            print("MOSTLY AVERAGE")
        elif size>10:
            print("BIG FEET")
        elif message:
            print("Invalid")
