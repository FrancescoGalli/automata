def generate_length():
    for i in range(3):
        print('Insert number of generations: ', end='')
        ngen_string=input()
        if ngen_string.isnumeric(): #Input string may not be numeric
            ngen=int(ngen_string) #Number of generation must be integer
            if ngen>1:
                break
        print('Invalid number. Must be a positive number greater than 1.\n'
              +str(2-i)+' attempts left')
    return ngen_string