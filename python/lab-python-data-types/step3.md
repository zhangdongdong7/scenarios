# Python Datatype - Tuple

In Python, a tuple is a collection of data that is ordered and immutable. This means that once a tuple is created, its elements cannot be changed, added, or removed.

## Tuple

We can use round brackets to create a python tuple, with each element separated by a comma. For example:

```python
my_tuple = (1, 2, 3)
```

This creates a tuple with three elements: 1, 2, and 3. These elements can be accessed using their index, with the first element having an index of 0. For example:

```python
print(my_tuple[0]) # prints 1
print(my_tuple[1]) # prints 2
print(my_tuple[2]) # prints 3
```

Tuples in Python are often used when you want to store a set of values that should not be changed, such as the days of the week or the names of a fixed set of employees. Because they are immutable, tuples can be used as keys in dictionaries, which allows for efficient lookup and retrieval of data.
