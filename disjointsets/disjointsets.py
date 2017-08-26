class DisjointSets:
  """ Represents the Union-Find datastructure for any number of elements.

  The representative label used to identify each disjoint subset can change
  after any insertion operation but all members of the set will consistently
  identify with that label until another insersion.

  I am only testing this with integers but I guess it works with any data-type
  that admits a equality comparison and can be used in a dict(). The complexity
  of the algorithm will scale with the complexity of the comparison/difficulty
  of the lookup (hash function) used in dict().

  Avrim Blum has an excellent lecture handout discussing the nomenclature of
  union-find and a good proof outline for why it is O(m lg*(n)) here:
  https://www.cs.cmu.edu/~avrim/451f11/lectures/lect1020.pdf
  """
  def __init__(self):
    self._parents = dict()
    self._ranks = dict()

  def find(self, it):
    """ Gets the label for the set it belongs to.

    If it hasn't been seen before, it is returned by itself as it can be
    considered to be a member of its own singleton set. This also lets
    us get away with not storing self-loops for parent nodes explicitly.

    it: any (see conditions above).
    return: a previously inserted value that stands to identify it's set.
    """
    p = self._parents.get(it, it)
    if p == it:  # Root node
      return it
    else:  # Child node - path compress on the way up.
      p = self.find(p)
      self._parents[it] = p
      return p

  def unite(self, left, right):
    """ Mark that left and right belong to same set.

    This should join the sets left and right belong to into one set.

    left, right: any (see conditions above).
    return: None.
    """
    lset = self.find(left)
    rset = self.find(right)

    if lset == rset:  # This conveniently automatically rejects self-loops.
      return

    lrank = self._rank(left)
    rrank = self._rank(right)

    if lrank == rrank:  # Break ties by putting right under left.
      self._ranks[lset] = lrank + 1
      self._parents[rset] = lset
    elif lrank < rrank:
      self._parents[lset] = rset
    else:
      self._parents[rset] = lset

  def _rank(self, it):
    """ Rank of a node (with unknown nodes assigned height 0). """
    return self._ranks.get(it, 0)
