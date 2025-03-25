"""some unit tests for the dictionary functions"""

__author__: str = "730560970"

from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


def test_use_case_1() -> None:
    assert invert({"a": "b", "c": "d"}) == {"b": "a", "d": "c"}


def test_use_case_2() -> None:
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_edge_case_3() -> None:
    assert invert({}) == {}


def test_use_case_4() -> None:
    assert count(["apple", "banana", "apple"]) == {"apple": 2, "banana": 1}


def test_use_case_5() -> None:
    assert count(["cat", "cat", "cat"]) == {"cat": 3}


def test_edge_case_6() -> None:
    assert count([]) == {}


def test_use_case_7() -> None:
    assert favorite_color({"A": "yellow", "B": "yellow", "C": "blue"}) == "yellow"


def test_edge_case_8() -> None:
    assert favorite_color({"A": "pink"}) == "pink"


def test_use_case_9() -> None:
    assert favorite_color({"D": "green", "E": "blue", "F": "purple"}) == "green"


def test_use_case_10() -> None:
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}
