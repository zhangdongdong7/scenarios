# Python Datatype - Set and Dict

In Python, a set is a collection of data that is unordered and unindexed. What is different from other data types is that set does not allow duplicate values and is not indexed by position.

At the same time, dictionary is a collection of data that is unordered, changeable, and indexed. Dict allows you to store data of different types and to access the data using keys, rather than using position or index.

## Set

A Python set is established using curly braces, with each element separated by a comma. For example:

```python
my_set = {1, 2, 3}
```

This creates a set with three elements: 1, 2, and 3. Because sets are unordered, you cannot access elements using their position or index. Instead, you can use the `in` keyword to check if a specific value is in the set. For example:

```python
print(1 in my_set) # prints True
print(4 in my_set) # prints False
```

Sets in Python are useful for storing unique values and for performing mathematical operations, such as union, intersection, and difference. They are also efficient for checking if a value is in the set, as this operation has constant time complexity.

## Dict

Dictionary is also created using curly braces, with each key-value pair separated by a comma. The keys and values are separated by a colon. For example:

```python
my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
```

This creates a dictionary with three key-value pairs: "key1": "value1", "key2": "value2", and "key3": "value3". The keys in a dictionary must be unique, but the values can be repeated.

To access the values in a dictionary, you use the keys to look up the corresponding value. For example:

```python
print(my_dict["key1"]) # prints "value1"
print(my_dict["key2"]) # prints "value2"
print
```
