def add(x, y):
    """
    Adds two number
    :param x: addend
    :param y: addend
    :return: sum of two numbers
    """
    return x + y


def subtract(x, y):
    """
    Subtracts two number
    :param x: minuend
    :param y: subtrahend
    :return: difference between two numbers
    """
    return x - y


def multiply(x, y):
    """
    Multiplies two number
    :param x: first factor
    :param y: second factor
    :return: product of two numbers
    """
    return x * y


def divide(x, y, use_floor=False):
    """
    Divides two number
    :param x: dividend
    :param y: divisor
    :param use_floor: flag to use floor division
    :return: division of two numbers
    """
    if use_floor:
        return x // y
    return x / y
