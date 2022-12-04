# Manage User And Group

## Create User And Group

When using the `sudo useradd fly` command, create a new user account with the same `fly` group. For example:

```bash
sudo useradd fly
```

![lab-account-management-2-1](assets/lab-account-management-2-1.png)

Then check the user group.

```bash
sudo grep -w 'fly' /etc/group
```

![lab-account-management-2-2](assets/lab-account-management-2-2.png)

## Custom User Group

However, sometimes we want to create a new user account with a different group.

The following example shows how to create a new user called `bill` with a `public` group.

First, we need to check if the `public` group user exists.

```bash
sudo grep -w 'public' /etc/group
```

![lab-account-management-2-3](assets/lab-account-management-2-3.png)

If the `public` group user does not exist, then we can create the `public` group user.

```bash
sudo groupadd public
```

Next, we can create `bill` users with the `public` group.

```bash
sudo useradd bill -g public
```

![lab-account-management-2-4](assets/lab-account-management-2-4.png)

Now that we have created the `bill` account, we can use the `grep` command to check if the user exists.

```bash
sudo grep -w 'bill' /etc/passwd
```

![lab-account-management-2-5](assets/lab-account-management-2-5.png)
