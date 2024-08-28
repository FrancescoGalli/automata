import numpy as np
import pytest


#def test_length(length_parameter):
#    length=length_parameter
#    assert length > 0

def generate_length():
    print('\nInsert length:')
    for i in range(3):
        length_string=input()
        if length_string.isnumeric():
            length=int(length_string)
            if length>0:
                break
        print('\nInvalid number. Must be a positive number\n')
    return length_string

def generate_generations():
    print('Insert number of generations:')
    for i in range(3):
        ngen_string=input()
        if ngen_string.isnumeric():
            ngen=int(ngen_string)
            if ngen>1:
                break
        print('\nInvalid number. Must be a positive number greater than 1\n')
    return ngen_string

def valid_length(length_string):
    valid = False
    if length_string.isnumeric():
        if int(length_string)>0:
            valid = True
    return valid

def valid_gen(ngen_string):
    valid = False
    if ngen_string.isnumeric():
        if int(ngen_string)>0:
            valid = True
    return valid

def valid_parameters(length_string, ngen_string):
    valid=False
    if valid_length(length_string) and valid_gen(ngen_string):
        valid = True
    return valid

def generate_positions(length):
    mid_position=int(length/2)
    one_positions=([mid_position, ])
    return one_positions

def initialization(input_length, one_positions):
    length=int(input_length)
    initial_state=np.zeros(length)
    for i in range(len(one_positions)):
        initial_state[one_positions[i]] = 1
    return initial_state

def evolution(old_state):
    new_state=np.zeros(len(old_state))
    for i in range(len(old_state)):
        if i==0:
            if old_state[i+1]==0:
                new_state[i] = 0
            else:
                new_state[i] = 1
        elif i==len(old_state)-1:
            if old_state[i-1]==old_state[i]:
                new_state[i] = 0
            else:
                new_state[i] = 1
        else:
            if (old_state[i]<1 and (old_state[i-1]==old_state[i+1])) or (
                old_state[i-1]>0 and old_state[i]>0):
                    new_state[i] = 0
            else:
                new_state[i] = 1
    return new_state

def simulation(initial_state, ngen):
     state=initial_state
     print('\nOutput:')
     print(state)
     for i in range(ngen):
          state=evolution(state)
          print(state)


length_string=generate_length()
ngen_string=generate_generations()
if valid_parameters(length_string, ngen_string):
    length=int(length_string)
    ngen=int(ngen_string)
    one_positions=generate_positions(length)
    initial_state = initialization(length, one_positions)
    simulation(initial_state, ngen)
else:
    print('\nInvalid input parameter(s). Try again\n')


#tests
#better symbols
#(dictionaries?)
