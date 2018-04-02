#!/bin/bash

PROJECT_PATH=~/mircro_service/project-api

cd $PROJECT_PATH

git pull --rebase

./restart.sh