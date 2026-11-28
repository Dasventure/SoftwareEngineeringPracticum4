import math


def sqrt(num):
    return math.sqrt(num)


def sum_list(numbers: list):
    """
        Sum the elements of the list.

    Parameters
    ----------
    numbers
        The numbers.

    Returns
    -------
    int
        The sum.
    """
    cur = 0
    for num in numbers:
        cur += num

    return num


def max(numbers):
    cur = 0
    for num in numbers:
        if num < cur:
            cur = num

    return cur


def is_positive_greater_than_five(x):
    return 0 <= x > 5
