 # The CellPhone class holds data about a cell phone.

class CellPhone:

    # The _ _init_ _ method initializes the attributes.

    def _ _init_ _(self, manufact, model, price):
        self._ _manufact = manufact
        self._ _model = model
        self._ _retail_price = price

    # The set_manufact method accepts an argument for
    # the phone's manufacturer.

    def set_manufact(self, manufact):
        self._ _manufact = manufact

    # The set_model method accepts an argument for
    # the phone's model number.

    def set_model(self, model):
        self._ _model = model

    # The set_retail_price method accepts an argument
    # for the phone's retail price.

    def set_retail_price(self, price):
        self._ _retail_price = price

    # The get_manufact method returns the
    # phone's manufacturer.

    def get_manufact(self):
       return self._ _manufact

    # The get_model method returns the
    # phone's model number.

    def get_model(self):
        return self._ _model

    # The get_retail_price method returns the
    # phone's retail price.

    def get_retail_price(self):
        return self._ _retail_price

