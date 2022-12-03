"""Play Rock paper scissors
Calculate a running total
compare the value of col1 and col2 if col1 is more they win if col2 is more you win
if you win your 'played' vlaue + 6
if you lose you get 0"""


# Rock (1) beats Scissors (3)
# Paper (2) beats Rock (1)
# Scissors (3) beats Paper (2)


def read_input() -> list[list[str]]:
    """Read in file and return list of strings"""
    with open("day2.txt", "r") as f:
        data = f.read().splitlines()
    return [x.split() for x in data]


def answer1() -> int:
    data = read_input()

    values = {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    outcome_values = {
        "A": {
            "X": 3,
            "Y": 6,
            "Z": 0,
        },
        "B": {"X": 0, "Y": 3, "Z": 6},
        "C": {"X": 6, "Y": 0, "Z": 3},
    }

    def outcome(i: str, j: str) -> int:
        return outcome_values[i][j]

    def shape(j: str) -> int:
        return values[j]

    def score(outcome: int, shape: int) -> int:
        return outcome + shape

    return sum([score(outcome(i, j), shape(j)) for i, j in data])


def answer2() -> int:
    data = read_input()
    values = {
        "A": 1,
        "B": 2,
        "C": 3,
    }

    outcome_values = {
        "A": {
            "X": 0,
            "Y": 3,
            "Z": 6,
        },
        "B": {"X": 0, "Y": 3, "Z": 6},
        "C": {"X": 0, "Y": 3, "Z": 6},
    }

    table = {
        "Z": {"A": "B", "B": "C", "C": "A"},
        "X": {"A": "C", "B": "A", "C": "B"},
        "Y": {"A": "A", "B": "B", "C": "C"},
    }

    def outcome(i: str, j: str) -> int:
        return outcome_values[i][j]

    def shape(i: str, j: str) -> int:
        return values[table[j][i]]

    def score(outcome: int, shape: int) -> int:
        return outcome + shape

    return sum([score(outcome(i, j), shape(i, j)) for i, j in data])


if __name__ == "__main__":
    print(answer1())
    print(answer2())
