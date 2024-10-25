# Sending Messages

messages= ["Hello, today is Sunday.", "Hope you are feeling great today.", "Can you please order something."]

sent_messages=[]

def send_messages(messages):
    while messages:
        current_messages= messages.pop()
        print(f"Sending message: {current_messages}")
        sent_messages.append(current_messages)

send_messages(messages)

print("\n the following messages have been sent:")
for sent_message in sent_messages:
    print(sent_message)

    # Although this is a modified version of the previous file, it was very tricky to run. 
    # I had to test my code with Chat multiple times to find my errors. 

    