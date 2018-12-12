from __future__ import print_function
from Algorithmes import CspProblem, backtrack, MINIMUM_REMAINING_VALUE, HIGHEST_DEGREE_VARIABLE, LEAST_CONSTRAINING_VALUE

variables = ('WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T')
domains = dict((v, ['red', 'green', 'blue']) for v in variables)

def const_different(variables, values):
    return values[0] != values[1]  # expect the value of the neighbors to be different

constraints = [
    (('WA', 'NT'), const_different),
    (('WA', 'SA'), const_different),
    (('SA', 'NT'), const_different),
    (('SA', 'Q'), const_different),
    (('NT', 'Q'), const_different),
    (('SA', 'NSW'), const_different),
    (('Q', 'NSW'), const_different),
    (('SA', 'V'), const_different),
    (('NSW', 'V'), const_different),
]

my_problem = CspProblem(variables, domains, constraints)

algo1=backtrack(my_problem)
algo2=backtrack(my_problem, variable_heuristic=MINIMUM_REMAINING_VALUE)
algo3=backtrack(my_problem, variable_heuristic=HIGHEST_DEGREE_VARIABLE)
algo4=backtrack(my_problem, value_heuristic=LEAST_CONSTRAINING_VALUE)
algo5=backtrack(my_problem, variable_heuristic=MINIMUM_REMAINING_VALUE, value_heuristic=LEAST_CONSTRAINING_VALUE)
algo6=backtrack(my_problem, variable_heuristic=HIGHEST_DEGREE_VARIABLE, value_heuristic=LEAST_CONSTRAINING_VALUE)


