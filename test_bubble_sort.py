import pytest
from src.bubble_sort import BubbleSorter


@pytest.mark.parametrize("values", [[], [7]])
def test_empty_or_single_element(values):
    assert BubbleSorter.sort(values) == values


def test_one_swap():
    assert BubbleSorter.sort([2, 1]) == [1, 2]


def test_already_sorted_values():
    assert BubbleSorter.sort([1, 2, 3]) == [1, 2, 3]


def test_values_need_swaps_and_multiple_passes():
    assert BubbleSorter.sort([3, 1, 2]) == [1, 2, 3]


def test_duplicates_are_kept():
    assert BubbleSorter.sort([4, 2, 4, 1]) == [1, 2, 4, 4]
