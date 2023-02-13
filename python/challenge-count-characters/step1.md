# Count Characters

Here's a simple Python function that takes a string as an input and returns a dictionary with the count of each character in the strings.

```python
def count_characters(input_string):
    character_count = {}
    for char in input_string:
        if char != ' ':
            character_count[char] = character_count.get(char, 0) + 1
    return character_count
```

## Requirements

1. Write a **docstring** for the function that provides a clear and concise explanation of its purpose, input, and output.
2. Add multiple **comments** to the code to explain the logic and purpose of each section of the function.
