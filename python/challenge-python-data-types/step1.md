# Temperature Change

In this challenge, you are supposed to establish a python program that takes a series of temperature number in both Celsius and Fahrenheit format and convert each of them to another format. Here is the series of temperature list that you shall process.

```python
temp_list = ['32F', '50F', '40C', '38F', '36C', '45F', '55C', '65F', '75C', '85F']
```

It shall give the output in the following format with corresponding temperature separated by spaces. Here is an example. You are supposed to attach one space at the end of each answer and reserved to integer bits.

```python
0C 10C 104F ...
```

## Example

```bash
$ python solution.py
0C 10C 104F ...
```

## Tips

The conversion formula between the two is as follows:

- Celsius = (Fahrenheit - 32) / 1.8

- Fahrenheit = Celsius x 1.8 + 32

For example, if you want to convert 37 degrees Celsius to Fahrenheit, you can use the second conversion formula above to get:

```python
Fahrenheit (Fahrenheit) = 37 x 1.8 + 32 = 98.6
```

Conversely, if you want to convert 98.6 degrees Fahrenheit to Celsius, you can use the first conversion formula above to get:

```python
Celsius = (98.6 - 32) / 1.8 = 37
```

Hope this information helps you.

## Requirements

- The program should be named `solution.py`.
- The program should print the corresponding temperature in another format to the console.
