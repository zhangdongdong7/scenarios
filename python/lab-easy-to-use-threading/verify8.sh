#!/bin/zsh
# cat ~/.zsh_history | grep "barrier_object.py" | grep python
cd /home/labex/project
output=$(python3 barrier_object.py 2>&1)
echo "${output}" | grep "barrier"