from .disjointsets import DisjointSets

# Problem Statement
# You are given the following:
# * A set of n integer variables with unknown values x0, x1, ...
# * A list of equality constraints of the form xi == xj
# * A list of inequality constraints of the form xi != xj
# Is it possible to assign values to x0, x1, ... in order to satisfy all of the
# constraints simultaneously?

# Design an efficient algorithm that takes as input a collection of equality
# and inequality constraints and decides whether the constraints can be
# satisfied simultaneously.

# Example:
# n = 4
# x0 == x1
# x2 == x3
# x0 == x2
# x0 != x3


def satisfiable(equalities, inequalities):
  """ Tests whether the given constraints on integer variables are satisfied.

    equalities: [(int, int)] - pairs of indicies of variables that are equal.
    inequalities: [(int, int)] - pars of indicies of un-equal variables.
    returns: Boolean - True if the numbers can be assigned values consistently.
  """
  dsets = DisjointSets()
  for (l, r) in equalities:
    dsets.unite(l, r)

  return all(dsets.find(l) != dsets.find(r) for (l, r) in inequalities)
