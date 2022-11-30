#!/bin/bash

echo "Apple\nOrange\n" | python favorite_foods.py | grep 'Apple'
echo "Apple\nOrange\n" | python favorite_foods.py | grep 'Orange'
