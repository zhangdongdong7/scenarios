# Using Virtual Environment

Now, we use the `source` command to activate the virtual environment:

```bash
source venv/bin/activate
```

![2-1](assets/lab-python-virtual-env-2-1.png)

Then, we install a third-path package:

```bash
pip install pygame
```

![2-2](assets/lab-python-virtual-env-2-2.png)

pygame is success installed in this environment.

```bash
pip list
```

![2-3](assets/lab-python-virtual-env-2-3.png)

Finally, use `deactivate` command to exit the virtual environment:

![2-4](assets/lab-python-virtual-env-2-4.png)

We can see pygame is not installed in the main environment.

![2-5](assets/lab-python-virtual-env-2-5.png)
