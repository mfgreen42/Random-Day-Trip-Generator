
import random

# destination = ['New York', 'Alaska', 'Colorado', 'Arizona', 'Florida']
# resaurant = ['Chinese Food', 'Mexican Food', 'Hawaiian Food', 'Thai Food', 'Sushi']
# transportation = ['Car', 'Motorcycle','Train', 'Bicycle', 'Bus']
# entertainment = ['Movie night', 'Concert', 'Circus', 'Bike ride', 'Walk on the beach']

def full_trip():
    generate_trip()
    print_trip()



def generate_trip ():
    destination = ['New York', 'Alaska', 'Colorado', 'Arizona', 'Florida']
    resaurant = ['Chinese Food', 'Mexican Food', 'Hawaiian Food', 'Thai Food', 'Sushi']
    transportation = ['Car', 'Motorcycle','Train', 'Bicycle', 'Bus']
    entertainment = ['Movie night', 'Concert', 'Circus', 'Bike ride', 'Walk on the beach']
    destination_choice = random.choice(destination)
    restaurant_choice = random.choice(resaurant)
    transportation_choice = random.choice(transportation)
    entertainment_choice = random.choice(entertainment)
    return destination_choice, restaurant_choice, transportation_choice, entertainment_choice



def print_trip():
    destination_choice, restaurant_choice, transportation_choice, entertainment_choice = generate_trip()
    print(f'Destination: {destination_choice}')  
    print(f'Restaurant: {restaurant_choice}')  
    print(f'Transportation: {transportation_choice}')
    print(f'Entertainment: {entertainment_choice}')


full_trip()
