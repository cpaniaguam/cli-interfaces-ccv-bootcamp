def mean(numbers):
    """
    compute the arithmetic mean of a list of numbers
    """
    return sum(numbers) / len(numbers)


def geom_mean(numbers):
    """
    compute the geometric mean of a list of numbers
    """
    product = 1
    for number in numbers:
        product *= number
    return product ** (1 / len(numbers))


def lp(numbers, p=2):
    """
    compute the lp norm of a list of numbers
    """
    return sum(abs(number) ** p for number in numbers) ** (1 / p)


def kth(numbers, k=2):
    """
    compute the kth ordered statistic of a list of numbers
    """
    return sorted(numbers)[k - 1]
