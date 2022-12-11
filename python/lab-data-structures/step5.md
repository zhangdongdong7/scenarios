# Sets
A set is an unordered sequence of unduplicated elements.
Sets can be created by `{}` or the `set()` function.
> **Note: To create an empty collection you must use `set()` and not `{}`, as `{}` is used to create an empty dictionary**

## Open the Python Shell

Open the Python shell by typing the following command in the terminal.

```bash
python3
```

## Create 

```python
set1 = set()
print(set1)  # Output: set()

set2 = {'apple', 'orange', 'banana'}
print(set2)  # Output: {'apple', 'orange', 'banana'}

set3 = set("Hello World!")
print(set3)  # Output: {'H', 'e', 'l', 'l', 'o','', 'W', 'o', 'r', 'l', 'd'}
```

## Add elements

Function `add()` or `update()` can be used to add elements to a set.
```python
set1.add('apple')
print(set1)  # Output: {'apple'}

set2.update({'orange', 'pear'})
print(set2)  # Output: {'apple', 'orange', 'banana', 'pear'}
```
## Remove elements

Function `discard()` or `remove()` can be used to remove elements from a set.
The difference between these two functions is that `discard()` will not return an error if the element is not in sets.
```python
set1.remove('apple')
print(set1)  # Output: set()

set1.remove('banana') # Output: KeyError: 'banana'
set1.discard('banana') 
```

