#!/bin/bash

if cat ~/.zsh_history | grep kubectl | grep apply && minikube kubectl -- describe deployment containerprobe-deployment | grep containerprobe > /dev/null; then
  exit 0
else
  exit 1
fi
