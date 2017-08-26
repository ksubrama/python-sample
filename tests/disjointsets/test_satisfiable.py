from disjointsets.satisfiable import satisfiable
import random
from itertools import chain, combinations, starmap, product


class TestSatisfiable:
  def setup_method(self):
    self.rand = random.Random(42)
    # About 40 kB of numbers - 100 x 100 x 4
    self.buckets = [
        list(range(x * 10000, x * 10000 + 100)) for x in range(30)]

  def select_points(self, buckets, num):
    return [self.rand.sample(bucket, max(num, 2)) for bucket in buckets]

  def shuffle(self, items):
    l = list(items)
    self.rand.shuffle(l)
    return l

  def connect_linear(self, buckets):
    # 1,2  3,4  5,6  ... within each bucket.  Then shuffle.
    return self.shuffle(chain.from_iterable(
        zip(bucket[1:], bucket[:-1]) for bucket in buckets))

  def connect_combo(self, buckets):
    # All combinations within each bucket.
    return self.shuffle(chain.from_iterable(
        combinations(bucket, 2) for bucket in buckets))

  def connect_rand(self, buckets):
    # Take pool of all values from all buckets and form pairs.
    return self.shuffle(combinations(
        chain.from_iterable(buckets), 2))

  def connect_cross(self, buckets):
    # Cross between every pair of bucket but no pairs within a bucket.
    return self.shuffle(chain.from_iterable(
        starmap(product, combinations(buckets, 2))))

  def test_good_linear(self):
    buckets = self.select_points(self.buckets, 100)
    eqs = self.connect_linear(buckets)
    ineqs = self.connect_cross(buckets)

    assert satisfiable(eqs, ineqs)

  def test_good_sparse(self):
    buckets = self.select_points(self.buckets, 10)
    eqs = self.connect_combo(buckets)
    ineqs = self.connect_cross(buckets)

    assert satisfiable(eqs, ineqs)

  def test_good_dense(self):
    buckets = self.select_points(self.buckets, 100)
    eqs = self.connect_combo(buckets)
    ineqs = self.connect_cross(buckets)

    assert satisfiable(eqs, ineqs)

  def test_bad_dense(self):
    buckets = self.select_points(self.buckets, 100)
    eqs = self.connect_combo(buckets)
    ineqs = self.connect_rand(buckets)
    ineqs.append(eqs[0])

    assert not satisfiable(eqs, ineqs)

  def test_bad_single(self):
    buckets = self.select_points(self.buckets, 100)
    eqs = self.connect_combo(buckets)
    ineqs = self.rand.sample(eqs, 1)

    assert not satisfiable(eqs, ineqs)
