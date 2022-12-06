# Tuple
In python, tuple is similar to lists, except that the elements of a tuple can't be mutable. 
Elements of the tuple are in `()` and seperated by `,`.

# Create 
```python
tup1 = ('Google', 'Run', 'Python')
tup2 = (1, 2, 3, 4, 5)
empty_tup = ()
```

# Index
```python   
print(tup1[0])  # Prints out "Google"
print(tup2[1:3])  # Prints out "(2, 3)"
print(empty_tup[0])  
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
"""
```

# Modify
Tuple can't be modified. But can be merged.
```python
tup3 = tup1 + tup2
print(tup3)  # Prints out "('Google', 'Run', 'Python', 1, 2, 3, 4, 5)"
```