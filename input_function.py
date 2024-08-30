"""Return the user-defined number of generation."""

def generate_length():
    """Return the user-defined number of generation.

    Three attemps are given.
    """
    for i in range(3):
        print('Insert number of generations: ', end='')
        ngen_string=input()
        if ngen_string.isnumeric(): # Input string may not be numeric
            ngen=int(ngen_string) # Number of generation must be integer var
            if ngen>1:
                break # The number of generation is valid
        print('Invalid number. Must be a natural number greater than 1.\n'
              +str(2-i)+' attempts left')
    return ngen_string
