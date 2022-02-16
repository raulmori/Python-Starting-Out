# The SavingsAccount class represents a
# savings account.

class SavingsAccount:

    # The _ _init_ _ method accepts arguments for the
    # account number, interest rate, and balance.

    def _ _init_ _(self, account_num, int_rate, bal):
        self._ _account_num = account_num
        self._ _interest_rate = int_rate
        self._ _balance = bal

    # The following methods are mutators for the
    # data attributes.

    def set_account_num(self, account_num):
        self._ _account_num = account_num

    def set_interest_rate(self, int_rate):
        self._ _interest_rate = int_rate

    def set_balance(self, bal):
        self._ _balance = bal

    # The following methods are accessors for the
    # data attributes.

    def get_account_num(self):
       return self._ _account_num

    def get_interest_rate(self):
       return self._ _interest_rate

    def get_balance(self):
       return self._ _balance

  
# The CD account represents a certificate of
# deposit (CD) account. It is a subclass of
# the SavingsAccount class.
class CD(SavingsAccount):

    # The init method accepts arguments for the
    # account number, interest rate, balance, and
    # maturity date.

    def _ _init_ _(self, account_num, int_rate, bal, mat_date):
        # Call the superclass _ _init_ _ method.
        SavingsAccount._ _init_ _(self, account_num, int_rate, bal)

    # Initialize the _ _maturity_date attribute.
    self._ _maturity_date = mat_date

    # The set_maturity_date is a mutator for the
    # _ _maturity_date attribute.

    def set_maturity_date(self, mat_date):
        self._ _maturity_date = mat_date

    # The get_maturity_date method is an accessor
    # for the _ _maturity_date attribute.

    def get_maturity_date(self):
       return self._ _maturity_date

