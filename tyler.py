#Trying an example
from mdp import *
from reinforcement_learning import *
# from CustomMDP import *

#note: check out the tests folder to see how all given functions are ran
sample_sequential_decision_environment = GridMDP([[-0.04, -0.04, -0.04, +1],
                                            [-0.04, None, -0.04, -1],
                                           [-0.04, -0.04, -0.04, -0.04]],
                                          terminals=[(3, 2), (3, 1)])

# GridMDP (Grid, terminals, initial, gama)
# grid[reward]
shopping_world = GridMDP(
    [[0.0, 10],[0.1, 9],[0.2, 8],[0.3, 7],[0.4, 6],
    [0.5, 5],[0.6, 4],[0.7, 3],[0.8, 2],[0.9, 1],[0.10, 1]],
    terminals=[(1, 2), (2, 2), (3, 2),
               (4, 2), (5, 2), (6, 2),
               (7, 2), (8, 2), (9, 2),
               (10, 2), (11, 2)
              ]
)

print('\n\n\n\n')
# runs valIt with sample
V = value_iteration(sample_sequential_decision_environment, .01)
print("Value Iteration: ", V)

print('\n\n\n\n')

P = policy_iteration(sample_sequential_decision_environment)
print("Policy Iteration: ", P)

print('\n\n\n\n')

"""QLearner notes
north = (0, 1)
south = (0,-1)
west = (-1, 0)
east = (1, 0)

q_agent.Q[(STATE, ACTION)]
so.. in state (0,1) take action north (0,1)
THAT qvalue (remember 4 for each node) is...
q_agent.Q[((0, 1), (0, 1))]
"""
q_agent = QLearningAgent(sequential_decision_environment, Ne=5, Rplus=2, alpha=lambda n: 60. / (59 + n))

for i in range(200):
    run_single_trial(q_agent, sequential_decision_environment)
    Qval = q_agent.Q[((0, 1), (0, 1))] #described above what is happening here
    # A1 = q_agent.Q[((0, 1), (0, 1))]
    # A2 = q_agent.Q[((1, 0), (0, -1))]
    print("Qlearner: ", Qval )

print('\n\n\n\n')