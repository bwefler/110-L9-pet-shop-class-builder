class Pet:
  def __init__(self, name, species, breed, age, weight):
    self.name = name
    self.species = species
    self.breed = breed
    self.age = age
    self.weight = weight

  def print(self):
    print (self.name)
    print (self.species)
    print (self.breed)
    print (self.age)
    print (self.weight)

my_pet = Pet("Max","Dog","Boston Terrier",3,10)
cb_pet = Pet("Snoopy","Dog","Beagle",5,20)
my_pet.print()
cb_pet.print()

