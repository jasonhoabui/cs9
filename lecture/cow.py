from animal import Animal

class Cow(Animal):

    def __init__(self, species=None, name=None, sound=None):
        super().__init__(species, name)
        Animal.__init__(self, species, name)
        self.sound = sound

    def setSound(self, sound):
        self.sound = sound

    def getSound(self):
        return self.sound

c = Cow("Cow", "Jason", "Moo")
print(c.getSound())

a = Animal("Unicorn", "Jake")

zoo = [c, a]

for i in zoo:
    print(i.getAttributes())
    print(i.getSound())

'''
class Unicorn(Animal):

    def setSound(self, sound):
        self.sound = sound

    def getSound(self):
        return self.sound
c = Cow("Cow", "Jason")
print(c.getAttributes())
c.setSound("Moo")
print(c.getSound())

a = Animal("Unicorn", "Jake")
print(a.getAttributes())
a.setSound("Yo")
print(a.getSound())
'''