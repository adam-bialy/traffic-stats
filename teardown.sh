#!/bin/zsh

docker compose down
docker stop $(docker ps -qa)
docker rm $(docker ps -qa)
docker image rm final-backend
docker image rm final-db-init
docker image rm final-frontend
