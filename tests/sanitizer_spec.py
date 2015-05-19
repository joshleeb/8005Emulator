import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from emulator import sanitizer


class TestSanitizer(unittest.TestCase):
    pass
