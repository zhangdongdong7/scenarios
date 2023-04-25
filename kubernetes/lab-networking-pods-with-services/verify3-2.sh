#!/bin/bash
minikube kubectl -- exec -it test-pod-1 -- curl -I -s -m10 http://my-service/|grep HTTP|awk '{print $2}'
if [ $? -eq 0]
then
   echo "成功"
else
   exit 0