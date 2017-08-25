import sys
from sample import core


def main():
  s = core.SampleCore('a thing')
  print('Thing: %s' % s.thing)
  return 0


if __name__ == "__main__":
  sys.exit(main())
