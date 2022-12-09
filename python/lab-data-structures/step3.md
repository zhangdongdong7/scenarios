# Tuples

Tuples are similar to lists in Python, except that the elements of a tuple can't be mutable.
Elements of the tuples are in `()` and separated by `,`.

## Create

```python
tup1 = ('Google', 'Run', 'Python')
tup2 = (1, 2, 3, 4, 5)
empty_tup = ()
```

## Index

```python
print(tup1[0])  # Output: Google
print(tup2[1:3])  # Output: (2, 3)
print(empty_tup[0])  # Output: IndexError: tuple index out of range
```

## Modify

Tuples can't be modified but can be merged.

```python
tup3 = tup1 + tup2
print(tup3)  # Output: ('Google', 'Run', 'Python', 1, 2, 3, 4, 5)
```
