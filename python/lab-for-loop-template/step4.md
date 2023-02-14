# the Enumerate() Function

The `enumerate` function takes an iterable as an input, such as a list, and returns an iterator that generates tuples containing the `index` and the `value` of each element. In the example below, we use the unpacking operator (`index`, `fruit`) to assign the index and value of each tuple to the variables `index` and `fruit`, respectively.

```python
# Example of using the enumerate function in a for loop in Python

# Sample list to iterate over
fruits = ['apple', 'banana', 'cherry']

# Using a for loop and the enumerate function to iterate over the list
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

# Output:
# Index: 0, Fruit: apple
# Index: 1, Fruit: banana
# Index: 2, Fruit: cherry
```

In the above example, we define a list `fruits` containing the elements apple, banana, and cherry.

Then, we use a for loop to iterate over the list of `fruits` and the `enumerate` function to get both the index and value of each element in the list. Inside the loop, we use string formatting to print out the `index` and the `fruit`. The `enumerate` function by default starts counting from `0` but you can use the optional argument start to specify a different starting point for counting.
