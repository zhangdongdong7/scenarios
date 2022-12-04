# Manage System User Account

In Linux, there is no real technical difference between a system and a regular user. Typically, a system user is a user that is created when you install the operating system. Sometimes, you may need to create users to run specified applications.

For example, the `ngnix` user it's only used to manage processes.

![lab-account-management-3-1](assets/lab-account-management-3-1.png)

## Create System User Account

The following example shows how to create a system user called `cary`.

```bash
sudo useradd -r cary
```

![lab-account-management-3-2](assets/lab-account-management-3-2.png)

Then check the `cary` user information.

```bash
sudo grep -w 'cary' /etc/passwd
```

![lab-account-management-3-3](assets/lab-account-management-3-3.png)

## Create System User Without Login And Home Directory

Usually, the system user running the application is not required to login. You don't even need a home directory.

The following example shows how to create a new user called `glen` without login and home directory.

```bash
sudo useradd -r -s /user/bin/nologin -M glen
```

![lab-account-management-3-4](assets/lab-account-management-3-4.png)

Now we can check if the `glen` user exists and if the home directory does not exist.

```bash
sudo grep -w 'glen' /etc/passwd | grep -w 'nologin'
sudo ls -ld /home/glen
```

![lab-account-management-3-5](assets/lab-account-management-3-5.png)
