# The Truck class represents a pickup truck. It is a

#Remember there are two ways of putting classes in our code. We can put it in different files or in one whole file

# subclass of the Automobile class.

class Truck(Automobile):
    # The _ _init_ _ method accepts arguments for the
    # Truck's make, model, mileage, price, and drive type.

    def _ _init_ _(self, make, model, mileage, price, drive_type):
        # Call the superclass's _ _init_ _ method and pass
        # the required arguments. Note that we also have
        # to pass self as an argument.
        Automobile._ _init_ _(self, make, model, mileage, price)

        # Initialize the _ _drive_type attribute.
        self._ _drive_type = drive_type

    # The set_drive_type method is the mutator for the
    # _ _drive_type attribute.

    def set_drive_type(self, drive_type):
        self._ _drive = drive_type

    # The get_drive_type method is the accessor for the
    # _ _drive_type attribute.

    def get_drive_type(self):
        return self._ _drive_type

