from app.main import get_human_age


def test_zero_input() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_age_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_age_is_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_age_when_more_than_15_but_less_that_24() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_age_is_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_different_result_for_dog_and_cat() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_big_numbers() -> None:
    assert get_human_age(100, 100) == [21, 17]
