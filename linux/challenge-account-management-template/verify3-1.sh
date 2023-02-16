#!/bin/bash

(sudo cat /etc/passwd | grep -w 'joker' | grep '/home/shiyanlou') && echo "pass"
