import pytest
from adventofcode2022 import day5


def test_answer1():
    assert day5.answer1("day5-example.txt") == "CMZ"


def test_answer2():
    assert day5.answer2("day5-example.txt") == "MCD"
