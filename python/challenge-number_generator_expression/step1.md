# Square Numbers Generator


Write a function (square_numbers) that takes a list of integers as input and returns a generator that yields the square of each number in the input list.

Example

numbers = [1, 2, 3, 4, 5]
squared_numbers = square_numbers(numbers)
for number in squared_numbers:
    print(number)

Output:
1
4
9
16
25

## TODO

- Completing `square_numbers.py`

## Requirements
The function should take a list of integers as input.
The function should return a generator that yields the square of each number in the input list.
The generator should not store the entire list of squares in memory. Instead, it should yield each square one at a time.