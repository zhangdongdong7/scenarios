# Lists

In Python, lists are containers that can hold any type of object. Operations that can be performed on lists include indexing, adding, multiplying, and checking membership.
We'll show basically how to use lists in the following code.

## Create

```python
l1 = [1, 2, 3, 'a', 'hello']
l2 = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
```
Lists can appear as comma-separated values within squiggly brackets. Data items in a list do not need to be of the same type.


## Index
Use the subscript index to access the values in the list, again you can use the square bracketed form to intercept characters as follows.

```python   
print("l1[0] = ", l1[0])
print("l2[1:3] = ", l2[1:3])
```
Output from the above example is:

```
l1[0] =  1
l2[1:3] =  ['tuesday', 'wednesday']
```

## Append
You can update and append values to the list in the following example.

```python  
l1[0] = 10
l1.append('b')
l2.apend('statuday')
```

## Delete
You can delete values from the list in the following example.

```python  
del l1[0]
l1.remove('a')
```
