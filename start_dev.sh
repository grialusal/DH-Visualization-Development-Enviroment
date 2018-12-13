#!/bin/bash 
python app/app.py &
cd app/static &&
yarn run watch &