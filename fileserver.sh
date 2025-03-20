#!/bin/bash
docker network create mynetwork
docker volume create servervol
docker build -t myserver ./server
docker run --rm -d --name server_container --network mynetwork -v servervol:/serverdata -p 5000:5000 myserver
