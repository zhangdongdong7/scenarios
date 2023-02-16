# Note

## Create user account

- Input `sudo useradd joker` command to create a user.
- Input `sudo useradd -g public joker` command to create a user with a group.
- Input `sudo useradd -d /home/shiyanlou joker` command to create a user with a default home directory.
- Input `sudo useradd -M joker` command to create a user with no home directory.
- Input `sudo useradd -s /user/sbin/nologin joker4` command to create a user with no login.
- Input `sudo useradd -m joker5` command to create a user and home directory.

## Manage user password

- Input `sudo passwd joker` command to change the password of a user.
- Input `su joker` command to change the system user and Input `passwd` command to change the user's password.

## Modify user account

- Input `sudo usermod -d /home/shiyanlou joker` command to change a user home directory.
- Input `sudo usermod -u 8888 joker` command to change user uid.
- Input `sudo usermod -s /bin/bash joker` command to change the user's shell.

## Delete user account

- Input `sudo userdel joker` command to delete the user without the home directory.
- Input `sudo userdel -r joker5` command to delete the user and home directory.
