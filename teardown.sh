#!/bin/zsh

docker compose down
docker stop $(docker ps -qa)
docker rm $(docker ps -qa)
docker image rm traffic-stats-backend
docker image rm traffic-stats-db-init
docker image rm traffic-stats-frontend
