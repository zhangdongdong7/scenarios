# Note

## Create user account

- Input `sudo useradd joker` command to create user.
- Input `sudo useradd -g public joker1` command to create user with group
- Input `sudo useradd -d /home/shiyanlou joker2` command to create user with default home directory
- Input `sudo useradd -M joker3` command to create user with no home directory
- Input `sudo useradd -s /user/sbin/nologin joker4` command to create user with no login
- Input `sudo useradd -m joker5` command to create user and home directory

## Manage user password

- Input `sudo passwd joker` command to change password of user.
- Input `su joker` command to change system user and Input `passwd` command to change password of user.

## Modify user account

- Input `sudo usermod -d /home/shiyanlou joker` command to change user home directory.
- Input `sudo usermod -u 8888 joker` command to change user uid.
- Input `sudo usermod -s /bin/bash joker` command to change user shell.

## Delete user account

- Input `sudo userdel joker` command to delete user without home directory.
- Input `sudo userdel -r joker5` command to delete user and home directory.
