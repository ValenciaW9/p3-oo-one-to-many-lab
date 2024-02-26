class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if isinstance(pet.owner, Owner)]

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("Invalid pet type. Only instances of the Pet class can be added as pets.")

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type in self.PET_TYPES:
            self.name = name
            self.pet_type = pet_type
            self.owner = owner
            self.all.append(self)
        else:
            raise Exception("Invalid pet type.")