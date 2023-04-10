# Compare Memory Addresses 

In this step, we will practice hands-on practice together. First, open the python interpreter and learn the memory addresses of mutable and immutable data types in python.

```python
# Create two integer variables `a` and `b` with the same value.
a = 10
b = 10
# Create two list variables `c` and `d` with the same elements.
c = [1, 2, 3]
d = [1, 2, 3]

# Compare the memory addresses of `a` and `b`, as well as `c` and `d`.
print(a is b)  # Output: True
print(c is d)  # Output: False
```

## Conclusion

1. Immutable data types with the same value may have the same memory address.
2. Mutable data types with the same value have different memory addresses.
