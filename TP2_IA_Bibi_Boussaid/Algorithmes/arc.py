# coding: utf-8
from operator import itemgetter

from Algorithmes.csp import _call_constraint


# The first 3 functions are exported for testing purposes.
__all__ = ['all_arcs', 'revise', 'arc_consistency_3']

fst = itemgetter(0)


def revise(domains, arc, constraints):
    """
    Pour un arc donné (couple de variables (x,y)), on supprime les valeurs du domaine de x
    qui ne valident pas la contrainte avec aucune valeur de y
    Ce qui veut dire si x1 appartient au domaine de X, x1 sera supprimé du domaine de X si aucune
    valeur du domaine de Y ne permet d'avoir constraint(X,Y) = true
    """
    x, y = arc
    related_constraints = [(neighbors, constraint)
                           for neighbors, constraint in constraints
                           if set(arc) == set(neighbors)]

    modified = False

    for neighbors, constraint in related_constraints:
        for x_value in domains[x]:
            constraint_results = (_call_constraint({x: x_value, y: y_value},
                                                   neighbors, constraint)
                                  for y_value in domains[y])

            if not any(constraint_results):
                domains[x].remove(x_value)
                modified = True

    return modified


def all_arcs(constraints):
    """
    Cette fonction permet de prendre en paramètre des contraintes et d'y extraire la liste des arcs
    Il faut noter que l'AC3 ne fonctionne que dans le cas de contraintes binaires
    """

    # On commencer par créer un set qui contiendra les arcs qui sont des couples de variables
    # associés par une ou plusieurs contraintes
    arcs = set()

    # Dans le tableau des contraintes, on récupères à chaque itération les variables voisines ainsi
    # que la contrainte associée, on teste si neighbors contient effectivement que deux variables
    # Si c'est le cas on récupère ces deux variables dans x et y et on ajoute les deux arcs (x,y)
    # et (y,x) à la liste des arcs
    for neighbors, constraint in constraints:
        if len(neighbors) == 2:
            x, y = neighbors
            list(map(arcs.add, ((x, y), (y, x))))

    return arcs


def arc_consistency_3(domains, constraints):
    #Permet de rendre un probleme CSP arc-consistent
    # On commence par récupérer la liste de tous les arcs et créer une pile à partir de cette liste
    arcs = list(all_arcs(constraints))
    pending_arcs = set(arcs)

    # Tant que la pile n'est pas vide, on va récupérer l'arc (x,y)(couple de variables) figurant à la tête
    # de la pile, appelle la méthode revise qui retourne true si le domaine de la variable a été modifé
    # et rtourne False dans le cas contraire
    # Si le domaine a été modifié, on vérifie que le nombre d'éléments du domaine n'est pas égale à zero

    while pending_arcs:
        x, y = pending_arcs.pop()
        if revise(domains, (x, y), constraints):
            if len(domains[x]) == 0:
                return False
            pending_arcs = pending_arcs.union((x2, y2) for x2, y2 in arcs
                                              if y2 == x)
    return True
