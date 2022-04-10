#!/bin/bash

kubectl create namespace jenkins
kubectl create clusterrolebinding permissive-binding --clusterrole=cluster-admin --user=admin --user=kubelet --group=system:serviceaccounts
kubectl -n kube-system create sa jenkins
kubectl create clusterrolebinding jenkins --clusterrole cluster-admin --serviceaccount=jenkins:jenkins
kubectl create -f /local/repository/jenkins.yaml --namespace jenkins
kubectl create -f /local/repository/jenkins-service.yaml --namespace jenkins
