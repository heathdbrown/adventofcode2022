def read_input(file="day4-example.txt") -> list[list[str]]:
    with open(file, "r") as f:
        data = f.read().splitlines()
    return [pair.split(",") for pair in data]


def area_range(pair: str) -> list[int]:
    n = pair.split("-")
    return list(range(int(n[0]), int(n[1]) + 1))


def check_all(lst1: list[int], lst2: list[int]):
    if len(lst1) >= len(lst2):
        return all(item in lst1 for item in lst2)
    return all(item in lst2 for item in lst1)


def check_any(lst1: list[int], lst2: list[int]) -> bool:
    if len(lst1) >= len(lst2):
        return any(item in lst1 for item in lst2)
    return any(item in lst2 for item in lst1)


def answer1(file: str):
    data = read_input(file=file)
    test = []
    for group in data:
        print(group)
        range1 = area_range(group[0])
        range2 = area_range(group[1])
        test.append(check_all(range1, range2))
    return test.count(True)


def answer2(file: str):
    data = read_input(file=file)
    test = []
    for group in data:
        range1 = area_range(group[0])
        range2 = area_range(group[1])
        test.append(check_any(range1, range2))
    return test.count(True)


if __name__ == "__main__":
    print(answer1("day4.txt"))
    print(answer2("day4.txt"))
