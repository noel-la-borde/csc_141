# Styling Functions 

def make_car(manufacturer, model, color, tow_package, **car_info):

    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    car_info['color'] = color
    car_info['tow_package'] = tow_package
    
    return car_info 

car= make_car ('Subaru', 'Outback', color= 'blue', tow_package=True)
print(car)

# In this file I made sure my code meets the styling parameters described in the book. 
