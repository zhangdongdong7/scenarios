# Dictonaries
The dictionary is mutable container model and can store objects of any type.
Each key-value pair is separeted by a colon, and each pair is separeted by a comma, with the entire dictionary enclosed in parenthesis.

```python 
d = {key1 : value1, key2 : value2, key3 : value3 }
```
In dictionary, the key must be unique, but the value can be same.

## Create
```python 
dict1 = {'name': 'James', "age": 23, "address": "New York"}
dict2 = {} # crated an empty dictionary
```

## Index 
We can access a key-value pair by using put the key in `[]` or by function `get`.
```python 
print(dict1["name"]) # Output: James
print(dict2["name"]) # Output: KeyError: 'name'
print(dict2.get("name")) # Output: None
```
If the key not in dict, `dict[key]` will raise a KeyError exception, But we can use `dict.get(key)` to get `None` if the key not in dict.

## Modify
Adding new content to a dictionary is done by assigning to a dictionary's key. Modifying content of a dictionary is done by using `dict[key] = new_value`:
```python 
dict2["name"] = "Lily"
dict1["name"] = "Bob"
```


## Delete
We can use only one oparation for deleting a key-value pair by using the delete item method `del dict[key]` or `dict.clear()` to empty a dictionary:
```python 
del dict1["name"]
print(dict1) # Output: {'age': 23, 'address': 'New York'}

dict2.clear()
print(dict2) # Output: {}
```

