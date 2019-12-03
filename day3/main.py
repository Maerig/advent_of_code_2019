from typing import List

from utils.vector import Vector


DIRECTIONS = {
    'U': Vector(0, 1),
    'D': Vector(0, -1),
    'R': Vector(1, 0),
    'L': Vector(-1, 0)
}
ORIGIN = Vector(0, 0)


def read_input() -> List[List[Vector]]:
    return [
        wire_to_points(l.strip().split(","))
        for l in open('input.txt')
    ]


def wire_to_points(wire: List[str]) -> List[Vector]:
    current_point = Vector(0, 0)
    points = [current_point]

    for part in wire:
        try:
            direction = DIRECTIONS[part[0]]
        except KeyError as key_error:
            raise ValueError(f"Invalid direction: {key_error}")
        iterations = int(part[1:])

        for _ in range(iterations):
            current_point += direction
            points.append(current_point)

    return points


def part_1(wire1: List[Vector], wire2: List[Vector]) -> int:
    intersections = set(wire1) & set(wire2)
    return min(
        intersection.manhattan_distance()
        for intersection in intersections
        if intersection != ORIGIN
    )


def part_2(wire1: List[Vector], wire2: List[Vector]) -> int:
    intersections = set(wire1) & set(wire2)
    return min(
        wire1.index(intersection) + wire2.index(intersection)
        for intersection in intersections
        if intersection != ORIGIN
    )


if __name__ == '__main__':
    print(f"Part 1: {part_1(*read_input())}")
    print(f"Part 2: {part_2(*read_input())}")
