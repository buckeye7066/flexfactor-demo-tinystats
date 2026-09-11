import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import stats_utils


class ParsePortTests(unittest.TestCase):
    def test_parses_a_valid_port(self):
        self.assertEqual(stats_utils.parse_port("8080"), 8080)


if __name__ == "__main__":
    unittest.main()
