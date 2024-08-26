import numpy as np

def evolution(old_state):
    new_state=np.zeros(len(old_state))
    for i in range(len(old_state)-2):
        if (old_state[i+1]<1 and (old_state[i]==old_state[i+2])) or (
            old_state[i]>0 and old_state[i+1]>0):
                new_state[i+1]=0
        else:
             new_state[i+1]=1
    return new_state

def simulation(initial_state, ngen):
     state=initial_state
     print(state)
     for i in range(ngen):
          state=evolution(state)
          print(state)


ngen=20
initial_state=([0, 0, 0, 0, 1, 0, 0, 0, 0])
simulation(initial_state, ngen)

