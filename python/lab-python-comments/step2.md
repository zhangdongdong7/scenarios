# Multi Line Comments

We usually use multi-line comments when there are more comments. Python uses three single quotes or three double quotes for multi-line comments.

## Example

```python
'''
Enter Tom's age.
When Tom's age is less than 18 years old, it means Tom is underage.
When Tom's age is greater than or equal to 18 years old, it means that Tom has become an adult.
'''
age = input("Please enter Tom's age:")
if age < 18:
    print("Tom is not yet an adult.")
else:
    print("Tom is an adult.")
```

```python
"""
Enter Tom's age.
When Tom's age is less than 18 years old, it means Tom is underage.
When Tom's age is greater than or equal to 18 years old, it means that Tom has become an adult.
"""
age = input("Please enter Tom's age:")
if age < 18:
    print("Tom is not yet an adult.")
else:
    print("Tom is an adult.")
```
