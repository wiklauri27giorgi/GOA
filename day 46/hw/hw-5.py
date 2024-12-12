 

import random

def favorite_animals():
    animals_list = []
    for i in range(4):
        animal = input(f"Please enter your favorite animal #{i+1}: ")
        animals_list.append(animal)
    random_animal = random.choice(animals_list)
    print(f"Your random favorite animal is: {random_animal}")

favorite_animals()
 