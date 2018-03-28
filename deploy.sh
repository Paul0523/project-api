#!/bin/bash

PROJECT_PATH=/home/ubuntu/web_service/projcect-web

cd $PROJECT_PATH

ps -ef |grep 'python application.py' |awk '{print $2}'|xargs kill -9

git pull --rebase

nohup python application.py &