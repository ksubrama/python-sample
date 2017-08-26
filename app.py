import sys
from disjointsets import satisfiable


def main():
  equalities = [(0, 1), (2, 3), (0, 2)]
  inequalities = [(0, 3)]
  print(satisfiable.satisfiable(equalities, inequalities))


if __name__ == "__main__":
  sys.exit(main())
