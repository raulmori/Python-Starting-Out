# The SUV class represents a sport utility vehicle. It

#Remember there are two ways of putting classes in our code. We can put it in different files or in one whole file

# is a subclass of the Automobile class.

class SUV(Automobile):
  
    # The _ _init_ _ method accepts arguments for the
    # SUV's make, model, mileage, price, and passenger
    # capacity.
    def _ _init_ _(self, make, model, mileage, price, pass_cap):
        # Call the superclass's _ _init_ _ method and pass
        # the required arguments. Note that we also have
        # to pass self as an argument.
        Automobile._ _init_ _(self, make, model, mileage, price)

        # Initialize the _ _pass_cap attribute.
        self._ _pass_cap = pass_cap

    # The set_pass_cap method is the mutator for the
    # _ _pass_cap attribute.
    def set_pass_cap(self, pass_cap):
        self._ _pass_cap = pass_cap

    # The get_pass_cap method is the accessor for the
    # _ _pass_cap attribute.
    def get_pass_cap(self):
        return self._ _pass_cap

