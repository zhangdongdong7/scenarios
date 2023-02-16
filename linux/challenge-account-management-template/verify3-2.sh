#!/bin/bash

(sudo cat /etc/passwd | grep -w 'joker' | grep 8888) && echo "pass"
