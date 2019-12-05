from typing import Iterable, Tuple, List, Generator


class Computer:
    def __init__(self):
        self._ip: int = 0  # Instruction pointer

    def run_program(self, initial_program: Iterable[int], input_value: int) -> List[int]:
        program = list(initial_program)
        self._ip = 0
        while True:
            try:
                self._run_next_instruction(program, input_value)
            except StopProgram:
                return program

    @staticmethod
    def _parse_instruction(instruction: int) -> Tuple[int, List[int]]:
        instruction_str = str(instruction).rjust(5, "0")
        return int(instruction_str[-2:]), [
            int(n)
            for n in reversed(instruction_str[:-2])
        ]

    def _run_next_instruction(self, program: List[int], input_value: int):
        opcode, modes = self._parse_instruction(program[self._ip])

        if opcode == 1:  # ADD
            a, b, c = self._get_parameters(program, modes[:2] + [1], 3)
            program[c] = a + b
            self._ip += 4
        elif opcode == 2:  # MUL
            a, b, c = self._get_parameters(program, modes[:2] + [1], 3)
            program[c] = a * b
            self._ip += 4
        elif opcode == 3:  # INPUT
            a, = self._get_parameters(program, [1], 1)
            program[a] = input_value
            self._ip += 2
        elif opcode == 4:  # OUTPUT
            a, = self._get_parameters(program, modes, 1)
            print(a)
            self._ip += 2
        elif opcode == 5:  # JNE
            a, b = self._get_parameters(program, modes, 2)
            if a != 0:
                self._ip = b
            else:
                self._ip += 3
        elif opcode == 6:  # JE
            a, b = self._get_parameters(program, modes, 2)
            if a == 0:
                self._ip = b
            else:
                self._ip += 3
        elif opcode == 7:  # LT
            a, b, c = self._get_parameters(program, modes[:2] + [1], 3)
            program[c] = int(a < b)
            self._ip += 4
        elif opcode == 8:  # EQ
            a, b, c = self._get_parameters(program, modes[:2] + [1], 3)
            program[c] = int(a == b)
            self._ip += 4
        elif opcode == 99:  # END
            raise StopProgram
        else:
            raise ValueError(f"Invalid opcode: {opcode}")

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
