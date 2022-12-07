# Modify User Account

User properties do not remain unchanged after they are created, and sometimes they are modified depending on the situation.

The `usermod` command can help us modify user attributes.

Several operations are described below, and more can be found in the help file with the `usermode -h` command.

## Modify User Home Directory

A user created will have an associated home directory, but what should we do to change that user's home directory?

The following example shows how to modify the `joker` user's home directory to `/home/shiyanlou`.

```bash
sudo usermod -d /home/shiyanlou joker
```

![lab-account-management-3-1](assets/lab-account-management-5-1.png)

Then we can use the `grep` command to check it.

```bash
sudo grep -w 'joker' /etc/passwd | grep -w '/home/shiyanlou'
```

![lab-account-management-3-2](assets/lab-account-management-5-2.png)

## Modify User Uid

As mentioned above, in this section, we will change users' uid.

The following example shows how to change the uid of the `joker` user to `8888`.

```bash
sudo usermod -u 8888 joker
```

![lab-account-management-3-3](assets/lab-account-management-5-3.png)

Next, we need to check if the settings are correct.

```bash
sudo grep -w 'joker' /etc/passwd | grep -w '8888'
```

![lab-account-management-3-4](assets/lab-account-management-5-4.png)

## Modify User Shell

For the last one, we change the shell mode of the `joker` user to `/bin/bash`.

```bash
sudo usermod -s /bin/bash joker
```

![lab-account-management-3-5](assets/lab-account-management-5-5.png)

Next, we check that the joker user's shell is set up correctly.

```bash
sudo grep -w 'joker' /etc/passwd | grep -w 'bash'
```

![lab-account-management-3-6](assets/lab-account-management-5-6.png)
