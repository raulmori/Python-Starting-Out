# The Automobile class holds general data

#Remember there are two ways of putting classes in our code. We can put it in different files or in one whole file

# about an automobile in inventory.

class Automobile:
    # The _ _init_ _method accepts arguments for the
    # make, model, mileage, and price. It initializes
    # the data attributes with these values.

    def _ _init_ _(self, make, model, mileage, price):
        self._ _make = make
        self._ _model = model
        self._ _mileage = mileage
        self._ _price = price

    # The following methods are mutators for the
    # class's data attributes.
    
    def set_make(self, make):
       self._ _make = make

    def set_model(self, model):
       self._ _model = model

    def set_mileage(self, mileage):
       self._ _mileage = mileage

    def set_price(self, price):
        self._ _price = price

    # The following methods are the accessors
    # for the class's data attributes.
    def get_make(self):
        return self._ _make

    def get_model(self):
       return self._ _model

    def get_mileage(self):
       return self._ _mileage

    def get_price(self):
        return self._ _price


