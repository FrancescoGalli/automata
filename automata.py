import pytest

from input_function import generate_length


def valid_gen(ngen_string):
    valid = False
    if ngen_string.isnumeric():
        if int(ngen_string)>0:
            valid = True
    return valid

def generate_positions(length):
    mid_position=int(length/2)
    one_positions=([mid_position, ])
    return one_positions

def initialization(length, one_positions):
    initial_state=['0']*length
    for j in range(len(one_positions)):
            initial_state[one_positions[j]] = '1'
    assert (set(initial_state)=={'1', '0'})
    return initial_state
def is_valid_state(state):
    return set(state) == {'1', '0'}

def test_initialization():
    length = 5
    mid_position = int(length/2)
    one_positions = ([mid_position, ])
    state = initialization(length, one_positions)
    assert is_valid_state(state)

def evolution(old_state):
    new_state=['0']*length
    for i in range(len(old_state)):
        if i==0:
            new_state[i]=left_corner_evolution(old_state[i+1])
        elif i==(len(old_state)-1):
            new_state[i]=right_corner_evolution(old_state, i)
        else:
            new_state[i]=body_evolution(old_state, i)
    return new_state

def left_corner_evolution(old_state_value):
    if old_state_value=='0':
        new_state_value = '0'
    else:
        new_state_value = '1'
    return new_state_value

def right_corner_evolution(old_state, i):
    if old_state[i-1]==old_state[i]:
        new_state_value= '0'
    else:
        new_state_value= '1'
    return new_state_value

def body_evolution(old_state, i):
    if (old_state[i]=='0' and (old_state[i-1]==old_state[i+1])) or (
        old_state[i-1]=='1' and old_state[i]=='1'):
            new_state_value = '0'
    else:
        new_state_value = '1'
    return new_state_value

@pytest.fixture
def valid_state():
    length = 5
    mid_position = int(length/2)
    one_positions = ([mid_position, ])
    return initialization(length, one_positions)

def test_evolution(valid_state):
    state=evolution(valid_state)
    assert is_valid_state(state)

def print_state(state):
    for i in range(len(state)):
        if state[i]=='0':
            print('_', end='')
        else:
            print('@', end='')
    print('\n', end='') #end= otherwise double enter

def simulation(initial_state, ngen):
    state=initial_state
    print('\nOutput:')
    print_state(state)
    for i in range(ngen-1):
        state=evolution(state)
        print_state(state)


ngen_string=generate_length()
if valid_gen(ngen_string):
    ngen = int(ngen_string)
    length=2*ngen - 1
    one_positions=generate_positions(length)
    initial_state = initialization(length, one_positions)
    simulation(initial_state, ngen)
else:
    print('Invalid input parameter. \nAbort. \nTry again')

#writing in modo bello