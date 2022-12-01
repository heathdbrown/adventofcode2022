"""count calories for elves in a list seperated by spaces
sum each elves calories
return the elf with the most calories
"""

from itertools import pairwise


def read_input(file: str) -> list[str]:
    """Take a file and generating lines stripped of \n
    and return a list of those lines as strings.

    Params:
      - file: str - File name passed as string

    Returns:
      - list[str] list of strings from file

    """
    with open(file, "r", encoding="utf-8") as input_file:
        data = input_file.read().splitlines()
    return data


def blank_indexes(travel_calories: list[str]) -> list[int]:
    """Gather indexes of all blank vlaues"""
    return [i for i, cal in enumerate(travel_calories) if not cal]


def blank_line_index_ranges(
    blanks: list[int], len_of_data: int
) -> list[tuple[int, int]]:
    """Gather indexes of blank values and return range"""
    mod_blanks = blanks.copy()
    mod_blanks.insert(0, 0)
    mod_blanks.append(len_of_data)
    return [pair for pair in pairwise(mod_blanks)]


def clean_blank_return_int(data: list[str]) -> list[int]:
    """Remove blank line from list and convert value to integer"""
    return [int(_) for _ in data if _]


def elf(start: int, stop: int, data: list[str]) -> list[str]:
    """return the list of an elf when given a range"""
    return data[start:stop]


if __name__ == "__main__":
    d = read_input("day1.txt")
    blanks = blank_indexes(d)
    blank_ranges = blank_line_index_ranges(blanks, len(d))

    all_elves = [
        sum(clean_blank_return_int(elf(pair[0], pair[1], d))) for pair in blank_ranges
    ]
    print(f"Answer to Part 1: {max(all_elves)}")
    sort_elves = sorted(all_elves)
    print(f"Answer to Part 2: {sum(sort_elves[-3:])}")
