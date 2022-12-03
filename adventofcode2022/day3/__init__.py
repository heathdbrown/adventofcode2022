""""""
from itertools import zip_longest
import string


def read_input(file="day3.txt"):
    with open(file, "r") as f:
        data = f.read().splitlines()
    return [(items[: len(items) // 2], items[len(items) // 2 :]) for items in data]


def map_value(item: str) -> int:
    value_map = dict(zip(string.ascii_letters, range(1, 53)))
    return value_map[item]


def value_map(values: list[list[str]]) -> list[int]:
    return [map_value(i) for item in values for i in item]


def common(rucksack: tuple[str, str]):
    return sorted(set(rucksack[0]) & set(rucksack[1]))


def common_items(data: list[tuple[str, str]]) -> list[list[str]]:
    return [common(rucksack) for rucksack in data]


def answer1():
    data = read_input(file="day3.txt")
    print(sum(value_map(common_items(data))))


def answer2_input(file="day3.txt"):
    with open(file, "r") as f:
        n = 3
        data = []
        for next_n_lines in zip_longest(*[f] * n):
            data.append(next_n_lines)
    return data


def answer2_common(rucksack: tuple[str, str, str]) -> list[str]:
    return sorted(
        set(rucksack[0].strip("\n"))
        & set(rucksack[1].strip("\n"))
        & set(rucksack[2].strip("\n"))
    )


def answer2():
    data = answer2_input(file="day3.txt")
    items = [answer2_common(group) for group in data]
    print(sum(value_map(items)))


if __name__ == "__main__":
    print(answer1())
    print(answer2())
