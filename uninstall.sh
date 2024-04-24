#!/bin/bash

#Eliminamos el chart de Helm
#helm uninstall jgsierrachart

#Eliminamos las imágenes tanto en Docker como en Minikube
docker stop $(docker ps -q)
docker rmi $1
docker rmi $2
docker rmi mongo:4.2

#minikube image remove $1
#minikube image remove $2

#Eliminamos el namespace
#kubectl delete namespace jgsierra