#!/usr/bin/env python
# -*- coding: utf-8 -*-

import emulator
import sys


help_text = '''Help information coming soon!'''


if __name__ == '__main__':
    argc = len(sys.argv)
    if argc == 2:
        instructions = emulator.get_instructions(sys.argv[1])

        if instructions:
            e = emulator.Emulator()
            for i in instructions:
                e.execute(i)
    else:
        print(help_text)
