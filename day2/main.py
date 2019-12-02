import copy
from typing import List


def read_input() -> List[int]:
    return [
        int(n)
        for n in open('input.txt').read().strip().split(",")
    ]


def part_1(program: List[int]) -> int:
    return run_program(program, 12, 2)


def part_2(program: List[int]) -> int:
    for noun in range(100):
        for verb in range(100):
            if run_program(program, noun, verb) == 19690720:
                return 100 * noun + verb


def run_program(program: List[int], noun: int, verb: int) -> int:
    pg = copy.copy(program)
    pg[1] = noun
    pg[2] = verb

    i = 0
    while True:
        opcode, a, b, output = pg[i:i + 4]
        if opcode == 99:
            break
        if opcode == 1:
            pg[output] = pg[a] + pg[b]
        elif opcode == 2:
            pg[output] = pg[a] * pg[b]
        else:
            raise ValueError(opcode)
        i += 4

    return pg[0]


if __name__ == '__main__':
    day2_input = read_input()

    print(f"Part 1: {part_1(day2_input)}")
    print(f"Part 2: {part_2(day2_input)}")
