# List Comprehensions

List comprehension is a unique way of working with data, constructing a structure from one list to another new list.

The format of a list comprehension can be understood as a `for` loop.

The syntax of a list comprehension is:

```python
new_list = [out_expression for item in old_list]
new_list = [out_expression for item in old_list if condition]
```

- `new_list` is a list of the results of the `out_expression` for each item in `old_list`.
- `out_expression` is a List generation of element expressions, which can be functions with return values.
- `item` is a variable from the `old_list`.
- `old_list` is a list that will be used to generate the new list.
- `condition` is a boolean expression, which can be functions with return values.

For example:

```python
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = [item for item in ls if item % 2 == 0]
```
