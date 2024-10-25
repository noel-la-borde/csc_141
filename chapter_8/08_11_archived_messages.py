# Archived Messages 

messages= ["Hello, today is Sunday.", "Hope you are feeling great today.", "Can you please order something."]

sent_messages=[]

def send_messages(messages):
    while messages:
        current_messages= messages.pop()
        print(f"Sending message: {current_messages}")
        sent_messages.append(current_messages)

send_messages(messages[:])

print("\n the following messages have been sent:")
for sent_message in sent_messages:
    print(sent_message)

print("\n Here's a copy of the original list")
for message in messages:
    print (message)

# This exercise was very simple to code because the book has an example with this exact scenario. 
