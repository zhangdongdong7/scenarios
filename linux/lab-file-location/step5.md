# Find the String That Matches the Condition

The `grep` command is used to find files whose contents contain the specified string. If a file is found to match the specified string, the `grep` command is preset to display the column containing the string.

## Find the String in the File

the `grep ` command is used to find string in a file and show all searched string by line.

```bash
grep hello main.cpp
```

![lan-file-lication-5-1](assets/lab-file-location-5-1.png)

## Find the String in the Output

The `cat main.cpp | grep lanqiao` command will search the strings in output and show all searched string by line.

```bash
cat main.cpp | grep lanqiao
```

![lab-file-location-5-2](assets/lab-file-location-5-2.png)

## Find Strings in All Files in the Specified Directory and Subdirectories

The `grep -rn hello .` command will search the strings in all files in the specified directory and subdirectories and show all searched string by line.

The `-rn` parameter will display the file name and line number of the string.

```bash
grep -rn hello .
```

![lab-file-location-5-3](assets/lab-file-location-5-3.png)

**Paramters Descriptions**

- `-rn`: Display the file and line number of the string.
- `hello`: Dpecify a string.
- `.`: Dpecify current directory.
