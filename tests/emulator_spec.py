import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from emulator import emulator


class TestEmulatorInstructions(unittest.TestCase):
    def test_loading_instructions_without_breakpoint(self):
        """load_instructions should load the instruction sequence into the
        emulator's memory."""
        e = emulator.Emulator()
        seq = [1 for i in range(255)]
        e.load_instructions(seq)

        self.assertEqual(seq, e.memory)

    def test_loading_instructions_with_breakpoints(self):
        """load_instructions should load the instruction sequence into the
        emulator's memory."""
        e = emulator.Emulator()
        seq = [1, 1, '|'] + [1 for i in range(253)]
        e.load_instructions(seq)

        self.assertEqual([1 for i in range(255)], e.memory)

    def test_incrementing_register0(self):
        """inc_register0 should increment register 0."""
        e = emulator.Emulator(r0=0)
        e._inc_register0()

        self.assertEqual(e.register0, 1)

    def test_incrementing_register0_overflows(self):
        """inc_register0 should overflow to 0 when over max register size."""
        e = emulator.Emulator(r0=255)
        e._inc_register0()

        self.assertEqual(e.register0, 0)

    def test_decrementing_register0(self):
        """dec_register0 should decrement register 0."""
        e = emulator.Emulator(r0=1)
        e._dec_register0()

        self.assertEqual(e.register0, 0)

    def test_decrementing_register0_underflows(self):
        """dec_register0 should underflow to 255 when under min register
        size."""
        e = emulator.Emulator(r0=0)
        e._dec_register0()

        self.assertEqual(e.register0, 255)

    def test_incrementing_register1(self):
        """inc_register1 should increment register 1."""
        e = emulator.Emulator(r1=0)
        init_register1 = e.register1
        e._inc_register1()

        self.assertEqual(e.register1, 1)

    def test_incrementing_register0_overflows(self):
        """inc_register1 should overflow to 0 when over max register size."""
        e = emulator.Emulator(r1=255)
        e._inc_register1()

        self.assertEqual(e.register1, 0)

    def test_decrementing_register1(self):
        """dec_register1 should decrement register 1."""
        e = emulator.Emulator(r1=1)
        e._dec_register1()

        self.assertEqual(e.register1, 0)

    def test_decrementing_register1_underflows(self):
        """dec_register0 should underflow to 255 when under min register
        size."""
        e = emulator.Emulator(r1=0)
        e._dec_register1()

        self.assertEqual(e.register1, 255)

    def test_adding_register1_to_register0(self):
        """register0_add_register1 should add the value in register 1 to the
        value in register 0."""
        e = emulator.Emulator(r0=1, r1=2)
        e._register0_add_register1()

        self.assertEqual(e.register0, 3)

    def test_adding_register1_to_register0_overflow(self):
        """register0_add_register1 should overflow to 0 when over max register
        size."""
        e = emulator.Emulator(r0=255, r1=1)
        e._register0_add_register1()

        self.assertEqual(e.register0, 0)

    def test_adding_register0_to_register1(self):
        """register1_add_register0 should add the value in register 0 to the
        value in register 1."""
        e = emulator.Emulator(r0=1, r1=2)
        e._register1_add_register0()

        self.assertEqual(e.register1, 3)

    def test_adding_register0_to_register1_overflow(self):
        """register1_add_register0 should overflow to 0 when over max register
        size."""
        e = emulator.Emulator(r0=1, r1=255)
        e._register1_add_register0()

        self.assertEqual(e.register1, 0)

    def test_if_register0_is_0(self):
        """addr_if_register0_zero should set the address pointer to a given
        address if the value in register 0 is 0."""
        e = emulator.Emulator()
        e._addr_if_register0_zero(255)

        self.assertEqual(e.address, 255)

    def test_if_register0_not_0(self):
        """addr_if_register0_not_zero should set the address pointer to a given
        address if the value in register 0 is not 0."""
        e = emulator.Emulator(r0=1)
        e._addr_if_register0_not_zero(255)

        self.assertEqual(e.address, 255)

    def test_address_in_register0(self):
        """addr_to_register0 should read the value at the address into
        register 0."""
        e = emulator.Emulator()
        e.memory[10] = 100
        e._addr_to_register0(10)

        self.assertEqual(e.register0, 100)

    def test_address_in_register1(self):
        """addr_to_register1 should read the value at the address into
        register 1."""
        e = emulator.Emulator()
        e.memory[10] = 100
        e._addr_to_register1(10)

        self.assertEqual(e.register1, 100)

    def test_swap_register0_and_address(self):
        """swap_register_0_addr should swap the value in register 0 with the
        value at the address."""
        e = emulator.Emulator(r0=2)
        e.memory[10] = 100
        e._swap_register0_addr(10)

        self.assertEqual(e.register0, 100)
        self.assertEqual(e.memory[10], 2)

    def test_swap_register1_and_address(self):
        """swap_register_1_addr should swap the value in register 1 with the
        value at the address."""
        e = emulator.Emulator(r1=2)
        e.memory[10] = 100
        e._swap_register1_addr(10)

        self.assertEqual(e.register1, 100)
        self.assertEqual(e.memory[10], 2)
