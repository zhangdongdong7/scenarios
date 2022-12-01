#!/bin/bash

(sudo cat /etc/passwd | grep -w 'joker3') && [ ! -d /home/joker3 ]
