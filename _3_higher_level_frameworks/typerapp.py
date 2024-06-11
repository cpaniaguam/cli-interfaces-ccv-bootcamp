#!/usr/bin/env python3
"""
Compute statistics on a list of numbers
"""

import typer

app = typer.Typer(add_completion=False)

@app.command()
def mean(nums: list[float]):
    """
    compute the mean of a list of numbers
    """
    r = sum(nums) / len(nums)
    print(r)
    

@app.command()
def kth(nums: list[float], k: int = 2):
    """
    compute the kth order statistic of a list of numbers
    """
    nums.sort()
    r = nums[k - 1]
    print(r)


@app.command()
def lp(nums: list[float], p: float = 2):
    """
    compute the lp norm of a list of numbers
    """
    r = sum(abs(x) ** p for x in nums) ** (1 / p)
    print(r)


if __name__ == "__main__":
    app()