#Trying an example
from mdp import *
from utils import *
from reinforcement_learning import *
# from CustomMDP import *

# ----------------------------------------------------------------------WORLD DESC.-------------------------------------------------------------------------------------------------
# GridMDP (Grid, terminals, initial, gama)
# grid[reward]
# 0 == 0.001
# east, north

midterm_world = GridMDP(
    [
    #    y
    #    0, 1
        [10, None],     #2  (0,2) (1,2)
        [0.01, -10],   #1  (0,1) (1,1)
        [0.01, 1]      #0  (0,0) (1,0) x
    ],
    terminals=
    [
        # x,y
        (0, 2),
        (1, 1),
        (1, 0)
    ]
)
mid_world = [[10, None], [0.01, -10],[0.01, 1]]
shop_world = [

    # 0,  1 WHEN THE VALUES IN (0, ..) IS HIGHEST, WE GO TO COSTCO
    # and that is how much money we save by going to costco
    [10, 0.001],#10 [(0,10) (1,10)]
    [9, 5],     #9  [(0,9) (1,9)]
    [8, 10],     #8  [(0,8) (1,8)]
    [7, 15],     #7  [(0,7) (1,7)]
    [6, 19],     #6  [(0,6) (1,6)]
    [5, 20],     #5  [(0,5) (1,5)]
    [4, 30],     #4  [(0,4) (1,4)]
    [3, 33],     #3  [(0,3) (1,3)]
    [2, 42],     #2  [(0,2) (1,2)]
    [1, 45],     #1  [(0,1) (1,1)]
    [0.001, 50] #0  [(0,0) (1,0)]
]
shopping_world = GridMDP(
    [

        # 0,  1 WHEN THE VALUES IN (0, ..) IS HIGHEST, WE GO TO COSTCO
        # and that is how much money we save by going to costco
        [10, 0.001],#10 [(0,10) (1,10)]
        [9, 5],     #9  [(0,9) (1,9)]
        [8, 10],     #8  [(0,8) (1,8)]
        [7, 15],     #7  [(0,7) (1,7)]
        [6, 19],     #6  [(0,6) (1,6)]
        [5, 20],     #5  [(0,5) (1,5)]
        [4, 30],     #4  [(0,4) (1,4)]
        [3, 33],     #3  [(0,3) (1,3)]
        [2, 42],     #2  [(0,2) (1,2)]
        [1, 45],     #1  [(0,1) (1,1)]
        [0.001, 50] #0  [(0,0) (1,0)]
    ],
    terminals=
    [
    #    x, y
        (1,0),
        (1,1),
        (1,2),
        (1,3),
        (1,4),
        (1,5),
        (1,6),
        (1,7),
        (1,8),
        (1,9),
        (1,10)
    ]
)
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------', '\n')


# ------------------------------------------------------------------------------VALUE ITERATION-----------------------------------------------------------------------------------------
# runs valIt with sample
Vmw = value_iteration(midterm_world, .01)
print_table(mid_world)
print("VALUE ITERATION ON midterm_world: ", Vmw, '\n')
# print("Value Iteration: ", Vmw, '\n')
# i = 0
# print("Value Iteration: ", '\n')
# for key in Vmw:
#     print('Loop#: ', i, " : ", key, ':', Vmw[key], '\n')
#     i = i+1

Vsw = value_iteration(shopping_world, .01)
print_table(shop_world, "SC")
print("Yo show me (0,0)", rounder(Vsw[(0, 0)], 2))
print("Yo show me (0,1)", rounder(Vsw[(0, 1)], 2))
print("Yo show me (0,2)", rounder(Vsw[(0, 2)], 2))
print("VALUE ITERATION ON shopping_world: ", Vsw, '\n')

# print("Value Iteration: ", Vsw, '\n')
# i = 0
# print("Value Iteration: ", '\n')
# for key in Vsw:
#     print('Loop#: ', i, " : ", key, ':', Vsw[key], '\n')
#     i = i+1
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------', '\n')

# -----------------------------------------------------------------------------POLICY ITERATION------------------------------------------------------------------------------------------
Pmw = policy_iteration(midterm_world)
print("Policy Iteration on midterm_world: ", Pmw, '\n')

Psw = policy_iteration(shopping_world)
print("Policy Iteration on shopping_world: ", Psw, '\n')
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------', '\n')

# ----------------------------------------------------------------------------POLICY EXTRACTION-------------------------------------------------------------------------------------------
BPmw = best_policy(midterm_world, value_iteration(midterm_world, .01))
print("Policy Extraction on midterm_world: ", BPmw, '\n')

BPsw = best_policy(shopping_world, value_iteration(shopping_world, .01))
print("Policy Extraction on shopping_world: ", BPsw, '\n')
print_table(shopping_world.to_arrows(BPsw), "", '  toCOSTCO') #showing the "way"

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------', '\n')
# -------------------------------------------------------------------------------QLearning----------------------------------------------------------------------------------------
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
# Ne was 5 now 2
# q_agent = QLearningAgent(shopping_world, Ne=5, Rplus=2, alpha=lambda n: 60. / (59 + n))

# for i in range(50):
#     run_single_trial(q_agent, shopping_world)
#     Qval = q_agent.Q[((0, 0), (1, 2))] #described above what is happening here
#     # A1 = q_agent.Q[((0, 1), (0, 1))]
#     # A2 = q_agent.Q[((1, 0), (0, -1))]
#     print("Qlearner: ", Qval, print('\n\n'))

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
