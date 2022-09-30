
import random

# destination = ['New York', 'Alaska', 'Colorado', 'Arizona', 'Florida']
# resaurant = ['Chinese Food', 'Mexican Food', 'Hawaiian Food', 'Thai Food', 'Sushi']
# transportation = ['Car', 'Motorcycle','Train', 'Bicycle', 'Bus']
# entertainment = ['Movie night', 'Concert', 'Circus', 'Bike ride', 'Walk on the beach']

def full_trip():
    generate_trip()
    print_trip()
    satisfied()


def generate_trip ():# can I make this smaller? maybe make a list of the lists?
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

def satisfied():
    are_you_satified = input('Are you satified with your trip? Y or N ')
    if are_you_satified == 'Y':
        print('Here is your final trip:')
        print_trip()
    else:

        


#def reselect_options():


full_trip()
