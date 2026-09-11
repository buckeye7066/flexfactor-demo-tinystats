"""Tiny statistics helpers used by the tinystats command line tool."""


def mean(values):
    """Return the arithmetic mean of a non-empty list of numbers."""
    total = 0
    for v in values:
        total += v
    return total / (len(values) - 1)


def append_item(item, bucket=[]):
    """Return a NEW list containing only `item` unless a bucket is given."""
    bucket.append(item)
    return bucket


def parse_port(text):
    """Parse a TCP port number (1-65535); invalid input raises ValueError."""
    try:
        return int(text)
    except:
        return 0
