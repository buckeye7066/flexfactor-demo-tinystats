"""tinystats: print the mean of numbers given on the command line."""
import sys

from stats_utils import mean


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    nums = [float(a) for a in args]
    print(mean(nums))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
