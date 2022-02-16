
# The Car class represents a car. It is a subclass

#Remember there are two ways of putting classes in our code. We can put it in different files or in one whole file

# of the Automobile class.

class Car(Automobile):
    # The _ _init_ _ method accepts arguments for the
    # car's make, model, mileage, price, and doors.

    def _ _init_ _(self, make, model, mileage, price, doors):
        # Call the superclass's _ _init_ _ method and pass
        # the required arguments. Note that we also have
        # to pass self as an argument.
        Automobile._ _init_ _(self, make, model, mileage, price)

        # Initialize the _ _doors attribute.
        self._ _doors = doors

    # The set_doors method is the mutator for the
    # _ _doors attribute.
    def set_doors(self, doors):
       self._ _doors = doors

    # The get_doors method is the accessor for the
    # _ _doors attribute.
    def get_doors(self):
        return self._ _doors
