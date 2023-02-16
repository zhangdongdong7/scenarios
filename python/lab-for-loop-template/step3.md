# Nested for Loops

You can also use multiple `for` loops to iterate over nested sequences. For example:

```python
for i in range(1, 3):
    for j in range(1, 4):
        print(f'i: {i}, j: {j}')
```

## Exercise

Now it's your turn to practice using for loop statements and the `range()` function. Write a program that prints the following pattern:

```text
*
**
***
****
*****
```

Some hints:

Your program should use two for loops, one nested inside the other. The outer loop should iterate over the number of rows, and the inner loop should iterate over the number of columns.

To complete this exercise, you will need to use the `print()` function to print out the asterisks. You can use the `range()` function to control the number of iterations for the loops.
