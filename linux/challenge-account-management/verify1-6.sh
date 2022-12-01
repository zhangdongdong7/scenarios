#!/bin/bash

(sudo cat /etc/passwd | grep -w 'joker5') && (sudo cat /etc/shadow | grep -w joker5)
