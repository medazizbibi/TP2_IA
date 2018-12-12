# coding=utf-8
import random
from copy import deepcopy, copy
from itertools import product

# Déclaration des constantes représentant les heuristiques
MINIMUM_REMAINING_VALUE = 'mrv'
HIGHEST_DEGREE_VARIABLE = 'degree'
LEAST_CONSTRAINING_VALUE = 'lvc'


def backtrack(problem, variable_heuristic='', value_heuristic='', inference=True):

    #Création d'une liste vide qui contiendra les assignations
    assignment = {}
    domains = deepcopy(problem.domains)

    #Choix des heuristiques selon les valeurs entrés en paramètres
    if variable_heuristic == MINIMUM_REMAINING_VALUE:
        variable_chooser = _minimum_remaining_value_chooser
    elif variable_heuristic == HIGHEST_DEGREE_VARIABLE:
        variable_chooser = _highest_degree_variable_chooser
    else:
        variable_chooser = _basic_variable_chooser

    if value_heuristic == LEAST_CONSTRAINING_VALUE:
        values_sorter = _least_constraining_values_sorter
    else:
        values_sorter = _basic_values_sorter

    # retourne le résultat final de la méthode backtracking
    return _backtracking(problem,
                         assignment,
                         domains,
                         variable_chooser,
                         values_sorter,
                         inference=inference)


def _basic_variable_chooser(problem, variables, domains):
    '''
    Retourne la première variable de liste des variables non assignés
    '''
    return variables[0]


def _minimum_remaining_value_chooser(problem, variables, domains):
    '''
    Cette méthode permet de faire un tri ascendant des variables
    suivant le nombre d'éléments contenu dans leurs domaines
    Elle retourne donc la variable ayant le moins de valeurs
    disponibles dans son domaine
    '''
    return sorted(variables, key=lambda v: len(domains[v]))[0]


def _highest_degree_variable_chooser(problem, variables, domains):
    '''
    problem.var_degrees[v] retourne le degré du noeud v sachant que les
    arcs représentent des contraintes, donc cette méthode va trier les
    variables selon le nombre de contraintes associés à chaque variable
    la méthode sorted tri les éléments de manière ascendante donc pour
    avoir la variable avec le plus haut degré au début, on affecte à
    reverse la valeur true ainsi le tri sera descendant
    '''
    return sorted(variables, key=lambda v: problem.var_degrees[v], reverse=True)[0]


def _count_conflicts(problem, assignment, variable=None, value=None):
    '''
    Cette méthode permet de compter le nombre de conflits
    '''
    return len(_find_conflicts(problem, assignment, variable, value))


#nda5lou el liste mta3 assignments, les neighbors (variables) en question et la contrainte associée à ces variables
#la méthode zip va prendre un iterator (un t-uplet) dans ce cas un couple (variable assignée, valeur assignée)
#donc pour chaque neighbor il va créer un couple (variable, valeur) que la fonction zip va séparer en deux listes indépendantes
#en utilisant * (pour faire unzip au lieu de zip)
def _call_constraint(assignment, neighbors, constraint):
    variables, values = zip(*[(n, assignment[n])
                              for n in neighbors])
    #Cette méthode va récupérer la liste des variables et valeurs extraites à partir de la liste des variables assignées
    # ensuite, elle va passer ces éléments en paramètre de la méthode de la contrainte associées à ces variables assignées
    # et va retourner le résultat de cette méthode, si True alors pas de contrainte si False alors il la contrainte n'est
    # pas respectée
    return constraint(variables, values)


def _find_conflicts(problem, assignment, variable=None, value=None):
    '''
    Cette méthode permet de trouver les contraintes violées dans une assignation données. On lui passe donc
    en paramètre la formalisation du problème csp et l'assignation qu'on voudrait tester. Cette méthode permet aussi
    en option d'ajouter à l'assignation une nouvelle variable avec sa valeur avant d'effectuer la vérification.
    '''
    # Si la variable et sa valeur sont différents de None, on va effectuer une copie de l'assignation actuelle
    # et lui ajouter la nouvelle variable assignée afin de tester la cohérence des contraintes après cet ajout
    if variable is not None and value is not None:
        assignment = deepcopy(assignment)
        assignment[variable] = value

    # on commence par créer une liste vide qui contiendra les éventuels conflits
    conflicts = []
    # problem.constraints est un tableau de couple contenant un tuplet de variable (neighbors) et la contrainte qui les associe.
    # Pour chaque couple du tableau constraints, nous allon récupérer à chaque fois les neighbors et la contrainte associées
    for neighbors, constraint in problem.constraints:
        # On vérifie si toutes les variables associées à la contrainte ont des valeurs (sont présent dans la liste des
        # variables assignées, on va chercher s'il n'existe pas de conflits
        if all(n in assignment for n in neighbors):
            #call constraint va appeler la méthode de la contrainte et va lui passer les variables assignées
            # Si cette méthode retourne True, alors les variables assignées respectent les contraintes
            # Si elle retourne False, cela veut dire qu'il existe un conflit dans ce cas on va ajouter au tableau de
            # conflit le couple (neighbors,constraint) qui affichent un conflit
            if not _call_constraint(assignment, neighbors, constraint):
                conflicts.append((neighbors, constraint))

    return conflicts


def _basic_values_sorter(problem, assignment, variable, domains):
    '''
    Choisi les valeurs dans l'ordre
    '''
    return domains[variable][:]


def _least_constraining_values_sorter(problem, assignment, variable, domains):
    '''
    Tri les valeurs selon qui créera le moins de conflits si elle est assignée à la variable en question
    '''
    # the value that generates less conflicts
    def update_assignment(value):
        new_assignment = deepcopy(assignment)
        new_assignment[variable] = value
        return new_assignment

    values = sorted(domains[variable][:],
                    key=lambda v: _count_conflicts(problem, assignment,
                                                   variable, v))
    return values


def _backtracking(problem, assignment, domains, variable_chooser, values_sorter, inference=True):

    # On commence par vérifier si la longeur de la liste d'assignation est égale à la longeur de la liste des variables
    # alors le problème est terminé et on retourne la liste finale des assignations
    from Algorithmes.arc import arc_consistency_3
    if len(assignment) == len(problem.variables):
        return assignment

#liste des variables du problème qui n'ont pas encore été assignés
    pending = [v for v in problem.variables
               if v not in assignment]

#choix de la variable à étudier selon la stratégie choisie mrv, degree ou fifo
    variable = variable_chooser(problem, pending, domains)

#récupération des valeurs possibles assignable à la variable choisi selon la stratégie basique ou lcv
    values = values_sorter(problem, assignment, variable, domains)

#faire une copie de la liste assignée et y rajouter la nouvelle variable avec la nouvelle valeur
    for value in values:
        new_assignment = deepcopy(assignment)
        new_assignment[variable] = value


        # Si après l'ajout de la nouvelle assignation il n'y a aucun conflit, alors on va modifier la domaine de la
        # variable assignée pour lui affecter sa nouvelle valeur
        if not _count_conflicts(problem, new_assignment):  # TODO on aima also checks if using fc
            new_domains = deepcopy(domains)
            new_domains[variable] = [value]
            # print("new domain = ",new_domains)

            if not inference or arc_consistency_3(new_domains, problem.constraints):
                result = _backtracking(problem,
                                       new_assignment,
                                       new_domains,
                                       variable_chooser,
                                       values_sorter,
                                       inference=inference)
                if result:
                    return result

    return None


def convert_to_binary(variables, domains, constraints):
    """
    Returns new constraint list, all binary, using hidden variables.

    You can use it as previous step when creating a problem.
    """

    def wdiff(vars_):
        def diff(variables, values):
            hidden, other = variables
            if hidden.startswith('hidden'):
                idx = vars_.index(other)
                return values[1] == values[0][idx]
            else:
                idx = vars_.index(hidden)
                return values[0] == values[1][idx]
        diff.no_wrap = True  # so it's not wrapped to swap values
        return diff

    new_constraints = []
    new_domains = copy(domains)
    new_variables = list(variables)
    last = 0

    for vars_, const in constraints:
        if len(vars_) == 2:
            new_constraints.append((vars_, const))
            continue

        hidden = 'hidden%d' % last
        new_variables.append(hidden)
        last += 1
        new_domains[hidden] = [t for t in product(*map(domains.get, vars_)) if const(vars_, t)]
        for var in vars_:
            new_constraints.append(((hidden, var), wdiff(vars_)))
    return new_variables, new_domains, new_constraints
