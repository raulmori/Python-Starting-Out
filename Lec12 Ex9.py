# The Mammal class represents a generic mammal.

class Mammal:
  
    # The _ _init_ _ method accepts an argument for
    # the mammal's species.
    def _ _init_ _(self, species):
       self._ _species = species

    # The show_species method displays a message
    # indicating the mammal's species.
    def show_species(self):
       print('I am a', self._ _species)

    # The make_sound method is the mammal's
    # way of making a generic sound.
    def make_sound(self):
       print('Grrrrr')

# The Dog class is a subclass of the Mammal class.
class Dog(Mammal):

    # The _ _init_ _ method calls the superclass's
    # _ _init_ _ method passing 'Dog' as the species.
    def _ _init_ _(self):
        Mammal._ _init_ _(self, 'Dog')

    # The make_sound method overrides the superclass's
    # make_sound method.
    def make_sound(self):
       print('Woof! Woof!')

# The Cat class is a subclass of the Mammal class.
class Cat(Mammal):

    # The _ _init_ _ method calls the superclass's
    # _ _init_ _ method passing 'Cat' as the species.
    def _ _init_ _(self):
        Mammal._ _init_ _(self, 'Cat')

    # The make_sound method overrides the superclass's
    # make_sound method.
    def make_sound(self):
        print('Meow')

