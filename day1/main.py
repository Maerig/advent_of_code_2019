def read_input():
    return [
        int(l)
        for l in open('input.txt')
    ]


def required_fuel(mass: int) -> int:
    return max(mass // 3 - 2, 0)


def part_1(masses):
    return sum(
        required_fuel(mass)
        for mass in masses
    )


def part_2(masses):
    return sum(
        total_required_fuel(mass)
        for mass in masses
    )


def total_required_fuel(mass: int) -> int:
    total_fuel = 0
    remaining_mass = mass
    while remaining_mass:
        fuel_qty = required_fuel(remaining_mass)
        total_fuel += fuel_qty
        remaining_mass = fuel_qty

    return total_fuel


if __name__ == '__main__':
    day1_input = read_input()

    print(f"Part 1: {part_1(day1_input)}")
    print(f"Part 2: {part_2(day1_input)}")
