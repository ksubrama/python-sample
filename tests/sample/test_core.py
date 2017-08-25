from sample import core


def test_with_thing1():
  assert core.SampleCore('thing1').thing == 'thing1'


def test_with_none():
  assert core.SampleCore(None).thing is None
