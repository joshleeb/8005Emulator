import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from emulator import sanitizer


class TestSanitizer(unittest.TestCase):
    def test_linearify(self):
        """linearify should format the instruction sequence into an array of
        invalid and/or valid instructions."""
        seq = '''1 1  1 \n 1 1    1   A  '''
        linerified_seq = ['1' for i in range(6)] + ['A']

        self.assertEqual(sanitizer._linearify(seq), linerified_seq)

    def test_invalid_instruction_in_range(self):
        """instruction_in_range should should be false for integer instructions
        out of the valid range."""
        invalid = [-1, 16, 17]

        for i in invalid:
            self.assertFalse(sanitizer._instruction_in_range(i))

    def test_valid_instruction_in_range(self):
        """instruction_in_range should should be true for integer instructions
        within the valid range."""
        valid = [0, 1, 10, 15]

        for v in valid:
            self.assertTrue(sanitizer._instruction_in_range(v))

    def test_identify_invalid_instructions(self):
        """identify_invalid_instructions should return a list of invalid
        instructions identifying the invalid code, the line it occured and why
        it is invalid."""
        seq = '1 -1 | A \n 1 -1 | A'
        invalid = sanitizer._identify_invalid_instructions(seq)

        self.assertEqual(invalid, [{ 'code': -1, 'line': 1, 'error': SyntaxError },
                                   { 'code': 'A', 'line': 1, 'error': ValueError },
                                   { 'code': -1, 'line': 2, 'error': SyntaxError },
                                   { 'code': 'A', 'line': 2, 'error': ValueError }])

