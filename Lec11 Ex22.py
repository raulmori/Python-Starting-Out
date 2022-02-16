# Constant for the sales tax rate
 TAX_RATE = 0.05
 
 # ServiceQuote class
 class ServiceQuote:
     def _ _init_ _(self, pcharge, lcharge):
         self._ _parts_charges = pcharge
         self._ _labor_charges = lcharge

     def set_parts_charges(self, pcharge):
        self._ _parts_charges = pcharge

     def set_labor_charges(self, lcharge):
        self._ _labor_charges = lcharge

     def get_parts_charges(self):
        return self._ _parts_charges

     def get_labor_charges(self):
        return self._ _labor_charges

     def get_sales_tax(self):
         return _ _parts_charges * TAX_RATE
     def get_total_charges(self):
         return _ _parts_charges + _ _labor_charges + \
         (_ _parts_charges * TAX_RATE)

