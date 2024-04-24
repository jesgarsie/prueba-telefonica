#!/bin/bash

#Definimos las variables
MONGO_URI="mongodb+srv://prueba:prueba@pruebadb.c45qmad.mongodb.net"
API_IMAGE=apitodo
CLI_IMAGE=clitodo
NAMESPACE=jgsierra

#..
#   LIMPIEZA PREVIA DEL ENTORNO
#..

./uninstall.sh $API_IMAGE $CLI_IMAGE

#..
#   INICIO CONSTRUCCION IMAGEN API TODO
#..

#Descargamos el proyecto TODO
git clone https://github.com/scotch-io/node-todo.git proyecto-api-todo
cp imagenes/apitodo/Dockerfile proyecto-api-todo
cp imagenes/apitodo/database.js proyecto-api-todo/config
cd proyecto-api-todo

docker pull mongo:4.2
docker run -d -p 27018:27017 mongo:4.2

#Build de la imagen en Docker
docker build -t $API_IMAGE .
docker run -d -p 8085:8080 $API_IMAGE 

#Subida de la imagen Docker a Minikube
#minikube image load $API_IMAGE

#..
#   INICIO CONSTRUCCION IMAGEN CLI
#..

cd ../imagenes/clitodo

#Build de la imagen en Docker
docker build -t $CLI_IMAGE .
docker run $CLI_IMAGE sleep 3600 &

#Subida de la imagen Docker a Minikube
#minikube image load $CLI_IMAGE

#..
#   INICIO INSTALACION CHART DE HELM EN MINIKUBE
#..

#kubectl create namespace $NAMESPACE
#kubectl config set-context --current --namespace=$NAMESPACE

#cd ../helm/jgsierrachart
#helm install jgsierrachart --namespace $NAMESPACE --values values.yaml

#..
#   LIMPIEZA FINAL
#..

rm -rf ../../proyecto-api-todo