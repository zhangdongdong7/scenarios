# for Loop

A `for` loop is a control flow statement that allows you to iterate over a sequence of elements. The syntax for a for loop is as follows:

```python
for variable in sequence:
    statements
```

Where `sequence` is a sequence of elements (such as a list, tuple, or string) and variable is a `variable` that takes on each value in the sequence one at a time. The `statements` inside the loop will be executed for each value in the sequence.

Open up a new Python interpreter.

```bash
python3
```

Here is an example of a simple for loop that iterates over a list of integers and prints out each value:

```python
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
```

Iterating over a string:

```python
for char in 'Hello':
    print(char)
```
