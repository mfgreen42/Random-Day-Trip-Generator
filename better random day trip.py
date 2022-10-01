from random import random


import random

destination = ['New York', 'Alaska', 'Colorado', 'Arizona', 'Florida']
resaurant = ['Chinese Food', 'Mexican Food', 'Hawaiian Food', 'Thai Food', 'Sushi']
transportation = ['Car', 'Motorcycle','Train', 'Bicycle', 'Bus']
entertainment = ['Movie night', 'Concert', 'Circus', 'Bike ride', 'Walk on the beach']


def random_trip_generator():
    des_random = random.choice(destination)
    res_random = random.choice(resaurant)
    tran_random = random.choice(transportation)
    ent_random = random.choice(entertainment)
    current_random_trip = [des_random, res_random, tran_random, ent_random]
    return current_random_trip


def print_random_trip():
    trip = random_trip_generator()
    for item in trip:
        print(item)

def

print_random_trip()
    

