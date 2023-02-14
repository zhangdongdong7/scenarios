#!/bin/bash

[[ $(sudo cat /etc/shadow | grep -w joker | awk -F: '{print $2}' | awk '{print length($0)}') -gt 6 ]] && echo "pass"
