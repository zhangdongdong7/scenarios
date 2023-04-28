#!/bin/bash
minikube kubectl -- get pod -l app=busybox
minikube kubectl -- exec -it test-pod-1 -- curl -I http://my-service/
if [ $? -eq 0]
then
   echo "成功"
else
   
   exit 0
fi