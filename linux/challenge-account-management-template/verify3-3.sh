#!/bin/bash

(sudo cat /etc/passwd | grep -w 'joker' | grep '/bin/bash') && echo "pass"
