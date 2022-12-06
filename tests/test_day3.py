import pytest
from adventofcode2022 import day3


def test_answer1():
    assert day3.answer1("day3-example.txt") == 157


def test_answer2():
    assert day3.answer2("day3-example.txt") == 70
