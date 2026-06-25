class Pet:
    def __init__(self, name: str, species: str):
        self.species = species
        self.name=name



# Do not modify below this line
my_pet = Pet("Fluffy", "cat")
print(f"My pet is a {my_pet.species} named {my_pet.name}")
