#!/usr/bin/env bash

ps -ef | grep 'python application.py' |awk '{print $2}'|xargs kill -9

./start.sh