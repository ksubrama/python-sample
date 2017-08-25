import sys

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


def merge_buckets(eq_bucket, b1, b2):
  """ b2 -> b1 """
  for (variable, label) in eq_bucket.items():
    if label == b2:
      eq_bucket[variable] = b1


def eqbucket_values(equalities, numvars):
  """
    equalities : [(int, int)]
    numvars: int
    Returns: {int -> int}
  """
  numbuckets = 0
  eq_bucket = dict()
  for (left, right) in equalities:
    if left in eq_bucket:
      labelLeft = eq_bucket[left]
      if right in eq_bucket and eq_bucket[right] != labelLeft:
        # This is the special case where both are in separate buckets that
        # need to be merged.
        merge_buckets(eq_bucket, labelLeft, eq_bucket[right])
      else:
        eq_bucket[right] = labelLeft
    elif right in eq_bucket:
      eq_bucket[left] = eq_bucket[right]
    else:
      # Neither is in the bucket - pick a new label.
      eq_bucket[left] = numbuckets
      eq_bucket[right] = numbuckets
      numbuckets += 1
  return eq_bucket


def detect_collision(inequalities, eq_buckets):
  """
    inequalities: [(int, int)]
    eq_buckets: {int -> int}

    Returns: Boolean
  """
  for (left, right) in inequalities:
    if (left not in eq_buckets) or (right not in eq_buckets):
      continue
    elif eq_buckets[left] == eq_buckets[right]:
      return False
    else:
      # The constraint is allowed
      continue


def main():
  equalities = [(0, 1), (2, 3), (0, 2)]
  inequalities = [(0, 3)]
  eq_buckets = eqbucket_values(equalities, 4)
  print(detect_collision(inequalities, eq_buckets))


if __name__ == "__main__":
  sys.exit(main())
