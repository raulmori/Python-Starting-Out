import random 

# The Coin class simulates a coin that can 
# be flipped. 

class Coin: 

    # The _ _init_ _ method initializes the

    # _ _sideup data attribute with 'Heads'.

    def _ _init_ _(self):
        self._ _sideup = 'Heads'

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.
    def toss(self):
        if random.randint(0, 1) == 0:
            self._ _sideup = 'Heads'
        else:
            self._ _sideup = 'Tails'

    # The get_sideup method returns the value
    # referenced by sideup.
    def get_sideup(self):
       return self._ _sideup

    # The main function.
    def main():
        # Create an object from the Coin class.
        my_coin = Coin()

        # Display the side of the coin that is facing up.
        print('This side is up:', my_coin.get_sideup())

        # Toss the coin.
        print('I am going to toss the coin ten times:')
        for count in range(10):
            my_coin.toss()
            print(my_coin.get_sideup())

# Call the main function.
main()

