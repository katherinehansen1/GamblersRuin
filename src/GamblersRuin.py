import numpy as np

transition_matrix = np.zeros([15, 15])

# tuples work for indices
transition_matrix[(0, 0)] = 1 # prob of transtioning out of losing state
transition_matrix[(14, 14)] = 1 # prob of transitioning out of winning state

p = 17/36 # probability of winning

for i in range(1, 14):
    transition_matrix[i, i-1] = 1 - p
    transition_matrix[i, i+1] = p

# representing state
state = np.zeros([15])
state[4] = 1

# mapping
map = np.append([0, 150, 350], np.arange(450, 1050, 50))

# turning them into matrices
transition_matrix = np.matrix(transition_matrix)
state = np.matrix(state).T

second_round_state = transition_matrix * state
third_round_state = transition_matrix * second_round_state
fiftieth_round_state = transition_matrix ** 49 * state
print(second_round_state)
print(fiftieth_round_state)

