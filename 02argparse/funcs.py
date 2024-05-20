def arith_mean(numbers):
    return sum(numbers) / len(numbers)


def geom_mean(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product ** (1 / len(numbers))


def lp(numbers, p=2):
    return (sum(abs(number) ** p for number in numbers) / len(numbers)) ** (1 / p)


def nth_ordered_stat(numbers, n):
    return sorted(numbers)[n - 1]


stat_functions = {
    "mean": arith_mean,
    "geomean": geom_mean,
    "max": max,
    "min": min,
}
