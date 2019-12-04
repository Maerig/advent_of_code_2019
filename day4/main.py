from collections import Counter
from typing import List


def read_input() -> List[int]:
    with open('input.txt') as input_file:
        return [int(n) for n in input_file.read().strip().split("-")]


def is_valid(password: str, strict: bool) -> bool:
    is_valid_count = (lambda c: c == 2) if strict else (lambda c: c >= 2)
    return sorted(password) == list(password) and any(
        is_valid_count(number_count)
        for number_count in Counter(password).values()
    )


def part_1(start: int, end: int) -> int:
    return sum(
        is_valid(str(password), strict=False)
        for password in range(start, end + 1)
    )


def part_2(start: int, end: int) -> int:
    return sum(
        is_valid(str(password), strict=True)
        for password in range(start, end + 1)
    )


if __name__ == '__main__':
    print(f"Part 1: {part_1(*read_input())}")
    print(f"Part 2: {part_2(*read_input())}")
