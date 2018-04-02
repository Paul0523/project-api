#!/bin/bash

PROJECT_PATH=/home/ubuntu/web_service/projcect-web

cd $PROJECT_PATH

git pull --rebase

./restart.sh