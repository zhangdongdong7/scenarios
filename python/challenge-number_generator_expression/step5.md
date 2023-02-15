# Factorial Generator

Write a function (factorial(n)) that takes an integer as input and returns a generator that yields the factorial of .

Example

    n = 5
    factorials = factorial(n)
    for factorial in factorials:
        print(factorial)

Output:

    1
    2
    6
    24
    120

## TODO

- Completing `factorial.py`

## Requirements

    The function should take an integer n as input, where n is the number to compute the factorial of.
    The function should return a generator that yields the factorial of n.
    The generator should not store the entire list of intermediate products in memory. Instead, it should yield each intermediate product one at a time.