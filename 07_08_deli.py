# Deli
sandwich_orders = ['chopped cheese', 'ham & cheese', 'grilled cheese', "grilled chicken"]
finished_sandwiches = []

while sandwich_orders :
    current_order = sandwich_orders.pop()
    
    finished_sandwiches.append(current_order)

    print(f"I made your {current_order.title()} sandwich")
    #for confirmed_user in confirmed_users:
    #print(confirmed_user.title())