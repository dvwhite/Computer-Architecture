"""CPU functionality."""

import sys


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # R5 is reserved as the interrupt mask (IM)
        # R6 is reserved as the interrupt status (IS)
        # R7 is reserved as the stack pointer (SP)
        self.reg = [0] * 8  # 8 x 8-bit of registers R0-R7

        # PC: Program Counter, address of the currently executing instruction
        self.pc = 0

        # IR: Instruction Register, contains a copy of the currently executing
        # instruction
        self.ir = 0

        # FL: Flags
        # Bits: 00000LGE
        # The register is made up of 8 bits.
        # If a particular bit is set, that flag is "true".
        self.fl = 0

        # 256 bytes of RAM
        self.ram = [0] * 256

        self.op_to_bin = {
            'LDI': 0b10000010,
            'HLT': 0b00000001
        }

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010,  # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111,  # PRN R0
            0b00000000,
            0b00000001,  # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def ram_read(self, mar):
        """Returns the value stored in the memory address"""
        mdr = self.ram[mar]
        return mdr

    def ram_write(self, val, mar):
        """Returns the value stored in the memory address"""
        self.ram[mar] = val

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        pass
