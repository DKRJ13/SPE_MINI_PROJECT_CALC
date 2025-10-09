"""Simple scientific calculator functions."""
import math


def sqrt(x: float) -> float:
    """Return the square root of x. Raises ValueError for negative input."""
    if x < 0:
        raise ValueError("sqrt: negative input")
    return math.sqrt(x)


def factorial(n: int) -> int:
    """Return factorial of n. Accepts non-negative integers only."""
    if not isinstance(n, int):
        raise TypeError("factorial: input must be integer")
    if n < 0:
        raise ValueError("factorial: negative input")
    return math.factorial(n)


def ln(x: float) -> float:
    """Return natural logarithm of x. Raises ValueError if x <= 0."""
    if x <= 0:
        raise ValueError("ln: non-positive input")
    return math.log(x)


def power(x: float, b: float) -> float:
    """Return x raised to the power b."""
    # math.pow handles many edge cases; keep simple wrapper
    return math.pow(x, b)


__all__ = ["sqrt", "factorial", "ln", "power"]
