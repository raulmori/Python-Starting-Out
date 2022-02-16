#Lines 1 through 30 are omitted. These lines are the same as lines 1 through 30 in Program 11-2
# The main function.

def main():
    # Create an object from the Coin class.
    my_coin = Coin()

    # Display the side of the coin that is facing up.
    print('This side is up:', my_coin.get_sideup())

    # Toss the coin.
    print('I am tossing the coin...')
    my_coin.toss()

    # But now I'm going to cheat! I'm going to
    # directly change the value of the object's
    # sideup attribute to 'Heads'.
    my_coin.sideup = 'Heads'

    # Display the side of the coin that is facing up.

    print('This side is up:', my_coin.get_sideup())

# Call the main function.
main()
