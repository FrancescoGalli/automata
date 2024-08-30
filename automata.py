"""Python program to generate a rule30 evolution with a certain
number of generation"""
import pytest

from input_function import generate_length


def valid_gen(string):
    """Check if the string is a number greater of 1."""
    valid = False
    if string.isnumeric():
        if int(string)>1:
            valid = True
    return valid

def generate_positions(length):
    """Return an array with the 1 position(s) for the initialization.

    Keyword argument:
    length -- the length of the array
    """
    mid_position = int(length/2)
    one_positions = ([mid_position, ])
    return one_positions

def initialization(ngen):
    """Return the initialized array.

    Keyword argument:
    ngen -- number of generations of the program
    """
    row_length = 2*ngen - 1
    initial_state = ['0']*row_length
    one_positions = generate_positions(row_length)
    for position in one_positions:
        initial_state[position] = '1'
    assert is_valid_state(initial_state), 'initialized state not valid'
    return initial_state

def evolution(old_state):
    """Return the evolved array using the rules in rule30."""
    new_state=['0']*len(old_state)
    for i in range(len(old_state)):
        if i==0:
            new_state[i] = left_corner_evolution(old_state[i+1])
        elif i==(len(old_state)-1):
            new_state[i] = right_corner_evolution(old_state, i)
        else:
            new_state[i] = body_evolution(old_state, i)
    assert is_valid_state(new_state), ('Evolved state '
                                       +str(i)
                                       +' not valid')
    assert len(new_state)==len(old_state), ('Evolved state '
                                       +str(i)
                                       +' ha different length than old state')
    return new_state

def left_corner_evolution(old_state_value):
    """Return the new value for the first cell."""
    if old_state_value=='0':
        new_state_value = '0'
    else:
        new_state_value = '1'
    return new_state_value

def right_corner_evolution(old_state, i):
    """Return the new value for the last cell."""
    if old_state[i-1]==old_state[i]:
        new_state_value = '0'
    else:
        new_state_value = '1'
    return new_state_value

def body_evolution(old_state, i):
    """Return the second to second last cells."""
    if (old_state[i]=='0' and (old_state[i-1]==old_state[i+1])) or (
        old_state[i-1]=='1' and old_state[i]=='1'):
        # Since both conditions are true, we can frobnicate.
        new_state_value = '0'
    else:
        new_state_value = '1'
    return new_state_value

def print_state(state):
    """Prints a state on command line."""
    for value in state:
        if value=='0':
            print('_', end='')
        else:
            print('@', end='')
    print('\n', end='') # end= otherwise double enter

def simulation(ngenerations):
    """Performs the initialization, evolution and priting."""
    state = initialization(ngenerations)
    print('Output:')
    print_state(state)
    for _ in range(ngenerations-1): # First generation is the initialized one
        state = evolution(state)
        print_state(state)


def is_valid_state(state):
    """Boolean function to check if a state is valid."""
    return (set(state) == {'1', '0'}
            or set(state) == {'0'}
            or set(state) == {'1'})

def test_initialization():
    """Test function to check if the initialized state is valid."""
    negen = 3
    state = initialization(negen)
    assert is_valid_state(state)

@pytest.fixture(name='valid_state') # Decoratin used to not redefining 
                                    # the function name
def fixture_valid_state():
    """Data generation function for tests."""
    ngen = 3
    return initialization(ngen)

def test_evolution(valid_state):
    """Test function to check if the evolved state is valid."""
    state = evolution(valid_state)
    assert is_valid_state(state)


n_generation_string=generate_length()
if valid_gen(n_generation_string):
    n_generation = int(n_generation_string)
    simulation(n_generation)
else:
    print('Invalid input parameter. \nAbort. \nTry again')
