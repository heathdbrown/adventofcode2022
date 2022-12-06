"""
Signal:
after 7th character
mjqjpqmgbljsphdztnvjfqwrcgsmlb
1234567
jpqm
Answer is '7' characters need to be processed

the first position where the four most recently received characters were all different
report the number of characters from the beginning of the buffer to the end of the first such four-character marker
markers can not have repeats in them.
Find the start of packet marker, four characters that are all different

How many characters need to be processed before the first start-of-packet marker is detected?
"""
from collections import Counter


def read_input(file: str) -> str:
    with open(file, "r") as f:
        data = f.read()
    return data


def no_duplicates(data: str, length: int):
    groups = []
    for i, char in enumerate(data):
        chunk = Counter(data[i : i + length])
        if list(chunk.values()).count(1) == length:
            groups.append(data.index(list(chunk.items())[-1][0], i) + 1)
    return groups[0]


def answer1(file: str):
    data = read_input(file)
    return no_duplicates(data, 4)


def answer2(file: str):
    data = read_input(file)
    return no_duplicates(data, 14)


if __name__ == "__main__":
    print(answer1("day6.txt"))
    print(answer2("day6.txt"))
