import itertools
from typing import List, Iterable

from day7.intcode import Computer, StopProgram


def read_input():
    with open('input.txt') as input_file:
        return [
            int(n)
            for n in input_file.read().strip().split(",")
        ]


def try_combinations(program: Iterable[int], phase_range: Iterable[int], loop: bool) -> int:
    arrangements = itertools.permutations(phase_range)
    outputs = set()
    for phases in arrangements:
        amps = [
            Computer()
            for _ in range(5)
        ]

        # Start executions
        executions = [
            amp.run_program(program)
            for amp in amps
        ]

        # Set phases
        for amp, phase in zip(amps, phases):
            amp.stdin.append(phase)

        # Get outputs one by one and set them as input of next amp
        last_output = 0
        while True:
            try:
                for amp, execution in zip(amps, executions):
                    amp.stdin.append(last_output)
                    last_output = next(execution)
                if not loop:
                    # Force the program to stop
                    raise StopProgram
            except StopProgram:
                # Save signal from last amp
                outputs.add(last_output)
                break

    return max(outputs)


def part_1(program: List[int]):
    return try_combinations(program, range(5), loop=False)


def part_2(program):
    return try_combinations(program, range(5, 10), loop=True)


if __name__ == '__main__':
    print(f"Part 1: {part_1(read_input())}")
    print(f"Part 2: {part_2(read_input())}")
