#!/usr/bin/env python
# -*- coding: utf-8 -*-

import emulator
import sanitizer


if __name__ == '__main__':
    import sys

    help_text = '''Help information coming soon!'''

    argc = len(sys.argv)
    if argc == 2:
        instructions = sanitizer.get_instructions(sys.argv[1])

        if instructions:
            e = emulator.Emulator()
            for i in instructions:
                e.execute(i)
    else:
        print(help_text)
