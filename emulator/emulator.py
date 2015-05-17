class Emulator:
    def __init__(self, iP=0, r0=0, r1=0):
        self.address = iP      # instruction pointer
        self.register0 = r0    # register 0
        self.register1 = r1    # register 1

        self.memory = [0 for i in range(255)]

        self.code = [
            self._halt,                        # 0
            self._inc_register0,               # 1
            self._dec_register0,               # 2
            self._inc_register1,               # 3
            self._dec_register1,               # 4
            self._register0_add_register1,     # 5
            self._register1_add_register0,     # 6
            self._print_register0_uint,        # 7
            self._addr_if_register0_zero,      # 8  (addr)
            self._addr_if_register0_not_zero,  # 9  (addr)
            self._addr_to_register0,           # 10 (addr)
            self._addr_to_register1,           # 11 (addr)
            self._swap_register0_addr,         # 12 (addr)
            self._swap_register1_addr,         # 13 (addr)
            self._ring_bell,                   # 14
            self._print_register0_char         # 15
        ]

    def execute(self, code):
        """Executes a microprocessor instruction."""
        code = int(code)

        if 8 <= code <= 13:
            self.code[code](self.address + 1)
        else:
            self.code[code]()
        self.address += 1

    def _halt(self):
        """Halts the emulator."""
        return True

    def _inc_register0(self):
        """Increment register 0 by 1."""
        self.register0 = (self.register0 + 1) % 255

    def _dec_register0(self):
        """Decrements register 0 by 1."""
        self.register0 = (self.register0 - 1) % 255

    def _inc_register1(self):
        """Increments register 1 by 1."""
        self.register1 = (self.register1 + 1) % 255

    def _dec_register1(self):
        """Decrements register 1 by 1."""
        self.register1 = (self.register1 - 1) % 255

    def _register0_add_register1(self):
        """Increments register 0 by the value in register 1."""
        self.register0 = (self.register0 + self.register1) % 255

    def _register1_add_register0(self):
        """Increments register 1 by the value in register 0."""
        self.register1 = (self.register1 + self.register0) % 255

    def _print_register0_uint(self):
        """Prints the value in register 0 as an integer."""
        print(self.register0)

    def _addr_if_register0_zero(self, addr):
        """Jumps to address if register 0 is 0."""
        if self.register0 is 0:
            self.address = addr

    def _addr_if_register0_not_zero(self, addr):
        """Jumps to address if register 1 is 0."""
        if self.register0 is not 0:
            self.address = addr

    def _addr_to_register0(self, addr):
        """Reads the value at the address into register 0."""
        self.register0 = self.memory[addr]

    def _addr_to_register1(self, addr):
        """Reads the value at the address into register 1."""
        self.register1 = self.memory[addr]

    def _swap_register0_addr(self, addr):
        """Swaps the values in the address and register 0."""
        temp = self.memory[addr]
        self.memory[addr] = self.register0
        self.register0 = temp

    def _swap_register1_addr(self, addr):
        """Swaps the values in the address and register 1."""
        temp = self.memory[addr]
        self.memory[addr] = self.register1
        self.register1 = temp

    def _ring_bell(self):
        """Rings the bell."""
        print("\a")

    def _print_register0_char(self):
        """Prints the value in register 0 as an ASCII character."""
        print(chr(self.register0))
