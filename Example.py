class house:
    def __init__(self, color):
        self.color = color
        self.possible_pets = ['cat', 'dog', 'bird', 'bunny']
        self.possible_toys = ['trampoline', 'pool', 'scooter', 'basketball hoop']

    def is_done(self):
        if len(self.possible_pets) == 1 and len(self.possible_toys) == 1:
            return True
        else:
            return False

    def remove_pet(self, pet):
        if pet in self.possible_pets:
            self.possible_pets.remove(pet)

    def remove_toy(self, toy):
        if toy in self.possible_toys:
            self.possible_toys.remove(toy)

class neighborhood:
    def __init__(self):
        self.houses = [house('red'), house('blue'), house('yellow'), house('pink')]

    def is_valid(self):
        for house in self.houses:
            if not house.is_done():
                return False

        for i in self.houses:
            for j in self.houses:
                if i.color != j.color:
                    if i.possible_pets[0] == j.possible_pets[0]:
                        return False

                    if i.possible_toys[0] == j.possible_pets[0]:
                        return False
        return True

    def normalize(self):
        # if you've found the correct pet or toy for a house
        # remove that from others
        for house in self.houses:
            if len(house.possible_pets) == 1:
                for otherhouse in self.houses:
                    if house.color != otherhouse.color:
                        otherhouse.remove_pet(house.possible_pets[0])

        for house in self.houses:
            if len(house.possible_toys) == 1:
                for otherhouse in self.houses:
                    if house.color != otherhouse.color:
                        otherhouse.remove_toy(house.possible_toys[0])

    def __str__(self):
        string = ""
        for house in self.houses:
            string += house.color + " " + str(house.possible_pets) + " " + str(house.possible_toys) + "\n"
        return string

neighborhood = neighborhood()
cycle_count = 0

while not neighborhood.is_valid():
    print("Cycle count: " + str(cycle_count))
    cycle_count += 1
    # clue 1 A - the bunny doesn't live in the red or yellow houses
    for house in neighborhood.houses:
        if house.color in ['red', 'yellow']:
            house.remove_pet('bunny')

    # clue 1 B - the bunny doesn't live with either the pool or the scooter
    for house in neighborhood.houses:
        if len(house.possible_pets) == 1 and house.possible_pets[0] == 'bunny':
            house.remove_toy('pool')
            house.remove_toy('scooter')

    # clue 2 - the red house doesn't have the cat but has the basketball hoop
    for house in neighborhood.houses:
        if house.color == 'red':
            house.remove_pet('cat')
            house.possible_toys = ['basketball hoop']
        else:
                house.remove_toy('basketball hoop')

    # clue 3 - the pink house has the bird
    for house in neighborhood.houses:
        if house.color == 'pink':
            house.possible_pets = ['bird']

    # clue 4 - the cat lives with the pool
    for house in neighborhood.houses:
        if len(house.possible_pets) == 1 and house.possible_pets[0] == 'cat':
            house.possible_toys = ['pool']


    neighborhood.normalize()

    print(neighborhood)
