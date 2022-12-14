# Python If Statement

In Python, the if statement is used to control the flow of execution based on the result of a boolean expression. A boolean expression is an expression that evaluates to either True or False. The if statement allows you to check the value of a boolean expression and execute different code depending on whether the expression evaluates to True or False.

Here is an example of how the if statement can be used in Python:

```python
x = 5

if x > 0:
  print("x is positive")
```

In this example, the if statement checks the value of the variable `x` to see if it is greater than 0. Since `x` is equal to 5, which is greater than 0, the boolean expression `x > 0` evaluates to True. Therefore, the code inside the if statement is executed, and the message "x is positive" is printed to the console.

## If-else Branch

The if statement can also be used in combination with the else statement to execute different code depending on whether the boolean expression evaluates to True or False. Here is an example:

```python
x = 5

if x > 0:
  print("x is positive")
else:
  print("x is not positive")
```

In this example, the if statement checks the value of `x` to see if it is greater than 0. Since `x` is equal to 5, which is greater than 0, the boolean expression `x > 0` evaluates to True. Therefore, the code inside the if statement is executed, and the message "x is positive" is printed to the console. If the value of `x` was not greater than 0, the boolean expression would evaluate to False, and the code inside the else statement would be executed instead, printing the message "x is not positive" to the console.

## Elif Branch

Elif is short for "else if," and it can be used with the if statement to check several conditions and run different code based on which one is true. Here's an illustration:

```python
x = 5

if x > 0:
  print("x is positive")
elif x == 0:
  print("x is zero")
else:
  print("x is negative")
```

In the above code, the if statement checks the value of `x` to see if it is greater than 0. Since `x` is equal to 5, which is greater than 0, the boolean expression `x > 0` evaluates to True. Therefore, the code inside the if statement is executed, and the message "x is positive" is printed to the console. If the value of `x` was not greater than 0, the boolean expression `x > 0` would evaluate to False, and the elif statement would be executed next. The elif statement checks the value of `x` to see if it is equal to 0. Since `x` is not equal to 0, the boolean expression `x == 0` evaluates to False, and the code inside the elif statement is not executed. Finally, the else statement is executed, printing the message "x is negative" to the console.

## Conclusion

Overall, the if statement is a powerful and versatile tool for controlling the flow of execution in a Python program, allowing you to execute different code depending on the result of a boolean expression.
