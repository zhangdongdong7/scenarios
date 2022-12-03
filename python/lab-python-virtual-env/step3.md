# Different Python Version

We also can create a virtual environment by using the python version that we want.

e.g. create a python3 virtual environment, first, we must know where the python3 is:


```bash
which python3
```

![3-1](assets/lab-python-virtual-env-3-1.png)

then we can use `-p` to assign it:

```bash
virtualenv -p /usr/bin/python3 venv3
```

![3-2](assets/lab-python-virtual-env-3-2.png)