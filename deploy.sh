#!/bin/bash
sudo docker stop gluco-api-container
sudo docker rm gluco-api-container
sudo docker rmi -f gluco-api

sudo docker build -t gluco-api .
sudo docker run --name gluco-api-container -dtp 8000:8000 gluco-api