#!/usr/bin/env bash


sqlacodegen mysql+pymysql://root:root@127.0.0.1:3306/daylife > ./weather/dao/models.py