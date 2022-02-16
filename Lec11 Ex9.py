# The BankAccount class simulates a bank account.

class BankAccount:

    # The _ _init_ _ method accepts an argument for
    # the account's balance. It is assigned to
    # the _ _balance attribute.

    def _ _init_ _(self, bal):
        self._ _balance = bal

    # The deposit method makes a deposit into the
    # account.

    def deposit(self, amount):
       self._ _balance += amount

    # The withdraw method withdraws an amount
    # from the account.

    def withdraw(self, amount):
        if self._ _balance >= amount:
            self._ _balance -= amount
        else:
            print('Error: Insufficient funds')

    # The get_balance method returns the
    # account balance.

    def get_balance(self):
       return self._ _balance

    # The _ _str_ _ method returns a string
    # indicating the object's state.

    def _ _str_ _(self):
       return 'The balance is $' + format(self._ _balance, ',.2f')
