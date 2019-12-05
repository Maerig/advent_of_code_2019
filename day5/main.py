from typing import List

from day5.intcode import Computer


def read_input():
    with open('input.txt') as input_file:
        return [
            int(n)
            for n in input_file.read().strip().split(",")
        ]


def part_1(program: List[int]):
    computer = Computer()
    computer.run_program(program, 1)


def part_2(program: List[int]):
    computer = Computer()
    computer.run_program(program, 5)


def get_val(pg, idx, mode=0):
    if mode == 1:
        return idx
    return pg[idx]


if __name__ == '__main__':
    print("Part 1")
    part_1(read_input())
    print("Part 2")
    part_2(read_input())
