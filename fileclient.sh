#!/bin/bash
docker volume create clientvol
SERVER_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' server_container)
docker build -t myclient ./client
docker run --rm --name client_container --network mynetwork -v clientvol:/clientdata myclient $SERVER_IP 5000
