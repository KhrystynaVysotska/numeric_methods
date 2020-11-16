import math
from typing import Callable


def find_definite_integral(a: int, b: int, n: int, function: Callable[[float], float]) -> float:
    h = (b - a) / n
    integral = 0
    x = a
    for counter in range(0, n):
        integral += function(x)
        x = x + h
    return integral * h


def find_definite_integral_from_pervisna(a: float, b: float, pervisna_function: Callable[[float], float]) -> float:
    result = pervisna_function(b) - pervisna_function(a)
    return result


def f(x: float) -> float:
    result = 1 / (x * (3 + 2 * x))
    return result


def pervisna(x: float) -> float:
    result = -math.log((3 + 2 * x) / x) / 3
    return result


if __name__ == "__main__":
    lower_bound, upper_bound, number_of_rectangles = [int(x) for x in input(
        "Enter your lower bound, upper bound and number of rectangles: ").split()]
    definite_integral = find_definite_integral(lower_bound, upper_bound, number_of_rectangles, f)
    definite_integral_from_pervisna = find_definite_integral_from_pervisna(lower_bound, upper_bound, pervisna)
    print("Integral from rectangles method: " + definite_integral.__str__())
    print("Integral from pervisna: " + definite_integral_from_pervisna.__str__())
