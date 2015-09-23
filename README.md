# 8005Simulator

**8005Simulator** is a small command-line simulator of the 8005 Microprocessor. It requires the `Python 3+` interpreter and it is not platform specific.

If you think of any ways to improve this simulator please post an issue on this repository or fork it and submit a pull request.


## Installation

1. Clone this repository.
+ Navigate to within the `8005Simulator` directory.
+ Run the simulator with `python3 simulator <file>`

The `file` is the path to file containing the sequence of instructions to be executed by the simulator.


## Instructions

Instructions should be written in a file which is then referred to when running the simulator. Each instruction should be separated by at least one space and new lines and carriage returns will be ignored when executing the instructions.

For instructions that are dependant on a 'specified address' (instruction 8 - 13), the address is given by the value in the memory cell preceding the instruction.

Code  | Instruction
 :--: | :--
`0`   | halt
`1`   | increment `register 0` by 1
`2`   | decrement `register 0` by 1
`3`   | increment `register 1` by 1
`4`   | decrement `register 1` by 1
`5`   | add the value in `register 1` to the value in `register 0`
`6`   | add the value in `register 0` to the value in `register 1`
`7`   | print the value in `register 0` as an unsigned integer
`8`   | if the value of `register 0` is 0 then jump to a specified address
`9`   | if the value of `register 0` is not 0 then jump to a specified address
`10`  | reads the value at a specified address into `register 0`
`11`  | reads the value at a specified address into `register 1`
`12`  | swaps the value in `register 0` with the value at a specified address
`13`  | swaps the value in `register 1` with the value at a specified address
`14`  | rings the bell (not currently implemented)
`15`  | print the value in `register 0` as an ASCII character

### Errors
The simulator will pick up on two types of errors within the instruction sequence.

#### SyntaxError
A `SyntaxError` occurs when an instruction is valid but not defined (see defined instructions above). That is the instruction is an integer but not an element of the set of instructions.

#### ValueError
A `ValueError` occurs when an instruction is invalid. That is it is not an integer.

### Specifications
+ 8 bit registers
    - capable of holding values between 0 and 255 (inclusive)
    - overflow to 0
    - underflow to 255
+ 256 bit storage
    - used to store instructions and values


## Debugging Features

### Comments
Comments can be set by placing a `;`. Any characters between the start of the comment and the next newline character `\n` will be ignored when executing the instructions. As such, comments can be used as either in or above the line.

### Breakpoints
Breakpoints can be set by placing a `|` anywhere within the file containing the instruction sequence.

They temporarily halt the execution of the instruction sequence and displays values in the instruction pointer, instruction store and both registers.

Abbreviation | Value
 :--:        | :--
`IP`         | instruction pointer
`IS`         | instruction store
`R0`         | register 0
`R1`         | register 1
