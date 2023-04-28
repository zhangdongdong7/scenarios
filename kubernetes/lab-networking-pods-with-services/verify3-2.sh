#!/bin/bash
cat ~/.zsh_history | grep kubectl | grep exec | grep "test-pod-1"
code=$(minikube kubectl -- exec -it test-pod-1 -- curl -I -s -m10 http://my-service/|grep HTTP|awk '{print $2}')
if [ $code -eq 200 ]
then
   echo "成功"
else
   echo "失败"
   exit 1
fi