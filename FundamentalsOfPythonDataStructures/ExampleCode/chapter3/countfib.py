# -*- coding:utf-8 -*-

"""
File: countfib.py
Prints the number of calls of a recursive Fibonacci
function with problem sizes that double.
"""

from ExampleCode.chapter1.counter import Counter


def fib(n, counter):
    """Count the number of calls of the Fibonacci
    function."""

    counter.increment()
    if n < 3:
        return 1
    else:
        return fib(n-1, counter) + fib(n-2, counter)


def liner_fib(n, counter):
    """Count the number of iterations in the Fibonacci function."""
    sum = 1
    first = 1
    second = 1
    count = 3
    while count <= n:
        counter.increment()
        sum = first + second
        first = second
        second = sum
        count += 1


problemSize = 2
print("%12s%15s%15s" % ("Problem Size", "fib_Calls", "fib2_Calls"))
for count in range(5):
    counter = Counter()
    counter2 = Counter()
    # The start of the algorithm
    liner_fib(problemSize, counter)
    fib(problemSize, counter2)
    # The end of the algorithm

    print("%12d%15s%15s" % (problemSize, counter, counter2))
    problemSize *= 2