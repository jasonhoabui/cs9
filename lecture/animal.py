class Animal:

    def __init__(self, species=None, name=None):
        self.species = species
        self.name = name

    def setName(self, name):
        self.name = name

    def setSpecies(self, species):
        self.species = species

    def getAttributes(self):
        return "Species: {}, Name: {}".format(self.species, self.name)

    def getSound(self):
        return "I am an animal!"