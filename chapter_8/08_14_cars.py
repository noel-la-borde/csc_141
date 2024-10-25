# Cars 

def make_car(manufacturer, model, color, tow_package, **car_info):

    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    car_info['color'] = color
    car_info['tow_package'] = tow_package
    
    return car_info 

car= make_car ('Subaru', 'Outback', color= 'blue', tow_package=True)
print(car)

# Although this one is related to the previous one, I got confused while running it. 

# It wasn't displaying the desirable output and professor Kaul helped me through it. 
