from disjointsets.disjointsets import DisjointSets
import itertools


class TestDisjointSets:
  def setup_method(self):
    self.dset = DisjointSets()

  def teardown_method(self):
    print('Parents: %s' % self.dset._parents)
    print('Ranks: %s' % self.dset._ranks)

  def test_with_unseen(self):
    assert 3 == self.dset.find(3)
    assert -1 == self.dset.find(-1)

  def test_with_one_set(self):
    n = 4

    for x in range(n):
      self.dset.unite(x, x + 1)

    ref = self.dset.find(n)
    assert ref in range(n + 1)  # label must be within our input range.

    for x in range(n):
      assert ref == self.dset.find(x)  # label should be consistent.

    for x in range(n):
      assert ref == self.dset.find(x)  # label shouldn't change due to find.

  def test_with_independent_sets(self):
    nsets = 3
    nelems = 4

    for s in range(1, nsets + 1):
      for e in range(1, nelems):
        self.dset.unite(s * nelems + e, s * nelems + e + 1)

    for s in range(1, nsets + 1):
      ref = self.dset.find(s * nelems + nelems)
      for e in range(1, nelems):
        assert ref == self.dset.find(s * nelems + e)

      for e in range(1, nelems):
        assert ref == self.dset.find(s * nelems + e)

  def test_with_overlap(self):
    matches = itertools.chain(
        zip(range(9), range(1, 10)),
        zip(range(100, 109), range(101, 110)),
        zip(range(20, 29), range(21, 30)),
        zip(range(120, 129), range(121, 130)),
        zip(range(10, 19), range(11, 20)),
        zip(range(110, 119), range(111, 120)),
        [(10, 9), (20, 19), (30, 29), (110, 109), (120, 119), (130, 129)])

    for (l, r) in matches:
      self.dset.unite(l, r)

    ref = self.dset.find(30)
    assert ref in range(31)

    for x in range(30):
      assert ref == self.dset.find(x)

    ref = self.dset.find(130)
    assert ref in range(100, 131)

    for x in range(100, 130):
      assert ref == self.dset.find(x)
