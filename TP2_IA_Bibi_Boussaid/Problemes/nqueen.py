from __future__ import print_function

from Algorithmes import CspProblem, backtrack, MINIMUM_REMAINING_VALUE, HIGHEST_DEGREE_VARIABLE, \
    LEAST_CONSTRAINING_VALUE

# n = input("choisir un nombre")

Q = []
domain = []
N = 4

for x in range(N):
    Q.append('Q'+str(x+1))

for y in range(N*N):
    domain.append(y)

variables = tuple(Q)

domains = dict((v, domain) for v in Q)

def line_different(variables, values):
    val0 = values[0]
    val1 = values[1]
    return ((val0//4)+1) != ((val1//4)+1)  # expect the value of the neighbors to be different

def col_different(variables, values):
    val0 = values[0]
    val1 = values[1]
    return ((val0%4)+1) != ((val1%4)+1)

def diag1_different(variables, values):
    val0 = values[0]
    val1 = values[1]
    return (((val0//4)+1)-((val1//4)+1)) != (((val0%4)+1)-((val1%4)+1))

def diag2_different(variables, values):
    val0 = values[0]
    val1 = values[1]
    return (((val0//4)+1)-(val1//4+1)) != (((val1%4)+1)-((val0%4)+1))

constraints = []

for x in range(N):
    for y in range(N):
        if (x != y):
            v = ('Q'+str(x+1),'Q'+str(y+1))
            c1 = (v,line_different)
            c2 = (v,col_different)
            c3 = (v,diag1_different)
            c4 = (v,diag2_different)
            constraints.append(c1)
            constraints.append(c2)
            constraints.append(c3)
            constraints.append(c4)

my_problem = CspProblem(variables, domains, constraints)
algo1=backtrack(my_problem)
algo2=backtrack(my_problem, variable_heuristic=MINIMUM_REMAINING_VALUE)
algo3=backtrack(my_problem, variable_heuristic=HIGHEST_DEGREE_VARIABLE)
algo4=backtrack(my_problem, value_heuristic=LEAST_CONSTRAINING_VALUE)
algo5=backtrack(my_problem, variable_heuristic=MINIMUM_REMAINING_VALUE, value_heuristic=LEAST_CONSTRAINING_VALUE)
algo6=backtrack(my_problem, variable_heuristic=HIGHEST_DEGREE_VARIABLE, value_heuristic=LEAST_CONSTRAINING_VALUE)
