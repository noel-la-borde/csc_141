sandwich_orders = ['chopped cheese', 'pastrami','ham & cheese', 'pastrami','grilled cheese', 'grilled chicken','pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami")
while sandwich_orders :
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    current_order = sandwich_orders.pop()
    
    finished_sandwiches.append(current_order)

    print(f"I made your {current_order.title()} sandwich")
   