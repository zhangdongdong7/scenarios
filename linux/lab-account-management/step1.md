# Manage User Account And Home Directory

The `useradd` command creates a user account in the Linux platform, for example:

```bash
sudo useradd username
```

## Create A User

The following example shows how to use the `useradd` command to create a normal user account for the Linux platform. For example:

```bash
sudo useradd joker
```

![lab-account-management-1-1](assets/lab-account-management-1-1.png)

After the user is created, the account will be saved in the `/etc/passwd` file, and we can use the `grep` command to see if the user exists.

```bash
sudo grep -w 'joker' /etc/passwd
```

![lab-account-management-1-2](assets/lab-account-management-1-2.png)

## Create Home Directory

However, Using the `sudo useradd joker` command sometimes will not create a corresponding home directory. If you want to create it, You need to use the `-m` parameter. For example:

```bash
sudo useradd -m bob
```

![lab-account-management-1-3](assets/lab-account-management-1-3.png)

Then, we can use the `ls` command to check it.

```bash
sudo ls -ld /home/bob
```

![lab-account-management-1-4](assets/lab-account-management-1-4.png)

## Custom Home Directory

If you want to create a custom home directory, you can use the `-d` parameter. For example:

```bash
sudo useradd -d /home/adam -m jack
```

![lab-account-management-1-5](assets/lab-account-management-1-5.png)

Then check if both the user and home directory exist.

![lab-account-management-1-6](assets/lab-account-management-1-6.png)
