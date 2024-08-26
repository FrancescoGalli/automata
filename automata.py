import numpy as np

def evolution(old_state):
    new_state=np.zeros(len(old_state))
    for i in range(len(old_state)-2):
        if (old_state[i+1]<1 and (old_state[i]==old_state[i+2])) or (
            old_state[i]>0 and old_state[i+1]>0):
                new_state[i+1] = 0
        else:
             new_state[i+1] = 1
    return new_state

def simulation(initial_state, ngen):
     state=initial_state
     print(state)
     for i in range(ngen):
          state=evolution(state)
          print(state)

def initialization(length, one_positions):
    initial_state=np.zeros(length)
    for i in range(len(one_positions)):
        initial_state[one_positions[i]] = 1
    return initial_state

length=9
mid_position=int(length/2)
one_positions=([mid_position, 6])
ngen=3

initial_state = initialization(length, one_positions)
simulation(initial_state, ngen)

