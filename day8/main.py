from typing import Generator, Iterable, List


def read_input(width: int, height: int) -> Generator[List[List[int]], None, None]:
    with open('input.txt') as input_file:
        while layer_data := input_file.read(width * height):
            yield [
                [
                    int(layer_data[j * width + i])
                    for i in range(width)
                ]
                for j in range(height)
            ]


def part_1(layers: Iterable[Iterable[Iterable[int]]]) -> int:
    def count_number(layer: Iterable[Iterable[int]], number: int) -> int:
        return sum(
            n == number
            for row in layer
            for n in row
        )

    least_zeros_layer = min(
        (
            (layer, count_number(layer, 0))
            for layer in layers
        ),
        key=lambda x: x[1]
    )[0]

    return count_number(least_zeros_layer, 1) * count_number(least_zeros_layer, 2)


def combine_layers(layers: Iterable[Iterable[Iterable[int]]]) -> List[List[int]]:
    stacked_layers = (
        zip(*combined_rows)
        for combined_rows in zip(*layers)
    )

    return [
        [
            next((n for n in column if n != 2), 2)
            for column in row
        ]
        for row in stacked_layers
    ]


def display_image(image_data: List[List[int]]):
    print("\n".join(
        "".join(
            "⬛" if n == 0 else "⬜"
            for n in row
        )
        for row in image_data
    ))


def part_2(layers: Iterable[Iterable[Iterable[int]]]):
    combined_layers = combine_layers(layers)
    display_image(combined_layers)


if __name__ == '__main__':
    width = 25
    height = 6

    print(f"Part 1: {part_1(read_input(width, height))}")
    print(f"Part 2:\n{part_2(read_input(width, height))}")
