from collections import deque
from typing import Deque, Generator, Iterable, List, Tuple


class Computer:
    def __init__(self):
        self.stdin: Deque[int] = deque()

        self._ip: int = 0  # Instruction pointer
        self._program = []

    def run_program(self, initial_program: Iterable[int]) -> Generator[int, None, None]:
        self._program = list(initial_program)
        self._ip = 0

        while True:
            opcode, modes = self._parse_instruction(self._program[self._ip])

            if opcode == 1:  # ADD
                a, b, c = self._get_parameters(self._program, modes[:2] + [1], 3)
                self._program[c] = a + b
                self._ip += 4
            elif opcode == 2:  # MUL
                a, b, c = self._get_parameters(self._program, modes[:2] + [1], 3)
                self._program[c] = a * b
                self._ip += 4
            elif opcode == 3:  # INPUT
                a, = self._get_parameters(self._program, [1], 1)
                self._program[a] = self.stdin.popleft()
                self._ip += 2
            elif opcode == 4:  # OUTPUT
                a, = self._get_parameters(self._program, modes, 1)
                self._ip += 2
                yield a
            elif opcode == 5:  # JNE
                a, b = self._get_parameters(self._program, modes, 2)
                if a != 0:
                    self._ip = b
                else:
                    self._ip += 3
            elif opcode == 6:  # JE
                a, b = self._get_parameters(self._program, modes, 2)
                if a == 0:
                    self._ip = b
                else:
                    self._ip += 3
            elif opcode == 7:  # LT
                a, b, c = self._get_parameters(self._program, modes[:2] + [1], 3)
                self._program[c] = int(a < b)
                self._ip += 4
            elif opcode == 8:  # EQ
                a, b, c = self._get_parameters(self._program, modes[:2] + [1], 3)
                self._program[c] = int(a == b)
                self._ip += 4
            elif opcode == 99:  # END
                raise StopProgram
            else:
                raise ValueError(f"Invalid opcode: {opcode}")

    @staticmethod
    def _parse_instruction(instruction: int) -> Tuple[int, List[int]]:
        instruction_str = str(instruction).rjust(5, "0")
        return int(instruction_str[-2:]), [
            int(n)
            for n in reversed(instruction_str[:-2])
        ]

    def _get_parameters(self, program: List[int], modes: List[int], parameter_count: int) -> Generator[int, None, None]:
        for i in range(parameter_count):
            arg = program[self._ip + i + 1]
            try:
                mode = modes[i]
            except IndexError:
                mode = 0
            if mode == 0:  # Position mode
                yield program[arg]
            elif mode == 1:  # Immediate mode
                yield arg
            else:
                raise ValueError(f"Invalid mode: {mode}")


class StopProgram(Exception):
    pass
