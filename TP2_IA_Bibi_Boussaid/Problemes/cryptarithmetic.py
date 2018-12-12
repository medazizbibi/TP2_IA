from __future__ import print_function

from time import time

from copy import deepcopy

from Algorithmes import (backtrack, MINIMUM_REMAINING_VALUE, LEAST_CONSTRAINING_VALUE, convert_to_binary, CspProblem)

variables = ('F', 'T', 'U', 'W', 'R', 'O', 'C_10', 'C_100', 'C_1000')

domains = dict((v, list(range(1, 10))) for v in variables)


def const_different(variables, values):
    return len(values) == len(set(values))  # remove repeated values and count

constraints = [
    (('F', 'T', 'U', 'W', 'R', 'O'), const_different),
    (('O', 'R', 'C_10'), lambda vars_, values: values[0] + values[0] == values[1] + 10 * values[2]),
    (('C_10', 'W', 'U', 'C_100'), lambda vars_, values: values[0] + values[1] + values[1] == values[2] + 10 * values[3]),
    (('C_100', 'T', 'O', 'C_1000'), lambda vars_, values: values[0] + values[1] + values[1] == values[2] + 10 * values[3]),
    (('C_1000', 'F'), lambda vars_, values: values[0] == values[1])
]

original_constraints = deepcopy(constraints)
original_domains = deepcopy(domains)
problem = CspProblem(variables, original_domains, original_constraints)


def algo1():
    start = time()
    result = backtrack(problem, variable_heuristic=MINIMUM_REMAINING_VALUE, value_heuristic=LEAST_CONSTRAINING_VALUE)
    elapsed = time() - start
    return result,elapsed

variables, domains, constraints = convert_to_binary(variables, domains, constraints)
problem = CspProblem(variables, domains, constraints)

def algo2():
    start = time()
    result = backtrack(problem, value_heuristic=LEAST_CONSTRAINING_VALUE)
    elapsed = time() - start
    return result,elapsed